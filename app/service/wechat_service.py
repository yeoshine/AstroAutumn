#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import time
from .. import app, redis
from flask import request, redirect
from wechat_sdk import WechatBasic
from ..models.user import User
from ..plugins.state import *
from instance import config


def check_signature(func):
    """
    微信签名验证
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')

        wechat = init_wechat_sdk()
        if not wechat.check_signature(signature=signature,
                                      timestamp=timestamp,
                                      nonce=nonce):
            if request.method == 'POST':
                return "signature failed"
            else:
                return redirect(app.config['MAIN_URL'])

        return func(*args, **kwargs)

    return decorated_function


def set_user_info(openid):
    """保存用户信息"""
    redis_prefix = "wechat:user:"
    cache = redis.hexists(redis_prefix + openid, 'nickname')

    if not cache:
        user_info = User.query.filter_by(openid=openid).first()
        if not user_info:
            try:
                wechat = init_wechat_sdk()
                user_info = wechat.get_user_info(openid)
                if 'nickname' not in user_info:
                    raise KeyError(user_info)
            except Exception as e:
                app.logger.warning(u"获取微信用户信息 API 出错: %s" % e)
                user_info = None
            else:
                user = User(openid=user_info['openid'],
                            nickname=user_info['nickname'],
                            sex=user_info['sex'],
                            province=user_info['province'],
                            city=user_info['city'],
                            country=user_info['country'],
                            headimgurl=user_info['headimgurl'])
                user.save()
                # 与查询的数据类型一样，方便 redis 写入
                user_info = user

        if user_info:
            # 写入缓存
            redis.hmset(redis_prefix + user_info.openid, {
                "nickname": user_info.nickname,
                "realname": user_info.realname,
                "classname": user_info.classname,
                "sex": user_info.sex,
                "province": user_info.province,
                "city": user_info.city,
                "country": user_info.country,
                "headimgurl": user_info.headimgurl,
                "regtime": user_info.regtime
            })
    else:
        timeout = int(time.time()) - int(get_user_last_interact_time(openid))
        if timeout > 24 * 60 * 60:
            try:
                wechat = init_wechat_sdk()
                user_info = wechat.get_user_info(openid)
                app.logger.warning(u"user_info: %s" % user_info)
                if 'nickname' not in user_info:
                    raise KeyError(user_info)
            except Exception as e:
                app.logger.warning(u"获取微信用户信息 API 出错: %s" % e)
            else:
                user = User.query.filter_by(openid=openid).first()
                user.nickname = user_info['nickname']
                user.sex = user_info['sex']
                user.province = user_info['province']
                user.city = user_info['city']
                user.country = user_info['country']
                user.headimgurl = user_info['headimgurl']
                user.update()

                redis.hmset(redis_prefix + openid, {
                    "nickname": user_info['nickname'],
                    "sex": user_info['sex'],
                    "province": user_info['province'],
                    "city": user_info['city'],
                    "country": user_info['country'],
                    "headimgurl": user_info['headimgurl']
                })
        return None

def is_user_exists(openid):
    """用户是否存在数据库"""
    redis_prefix = "wechat:user:"
    cache = redis.exists(redis_prefix + openid)
    if not cache:
        user_info = User.query.filter_by(openid=openid).first()
        if not user_info:
            return False
        else:
            return True
    else:
        return True

def init_wechat_sdk():
    """初始化微信 SDK"""
    access_token = redis.get("wechat:access_token")
    jsapi_ticket = redis.get("wechat:jsapi_ticket")
    token_expires_at = redis.get("wechat:access_token_expires_at")
    ticket_expires_at = redis.get("wechat:jsapi_ticket_expires_at")
    if access_token and jsapi_ticket and token_expires_at and ticket_expires_at:
        wechat = WechatBasic(appid=app.config['APP_ID'],
                             appsecret=app.config['APP_SECRET'],
                             token=app.config['TOKEN'],
                             access_token=access_token,
                             access_token_expires_at=int(token_expires_at),
                             jsapi_ticket=jsapi_ticket,
                             jsapi_ticket_expires_at=int(ticket_expires_at))
    else:
        wechat = WechatBasic(appid=app.config['APP_ID'],
                             appsecret=app.config['APP_SECRET'],
                             token=app.config['TOKEN'])
        access_token = wechat.get_access_token()
        redis.set("wechat:access_token", access_token['access_token'], 7000)
        redis.set("wechat:access_token_expires_at",
                  access_token['access_token_expires_at'], 7000)
        jsapi_ticket = wechat.get_jsapi_ticket()
        redis.set("wechat:jsapi_ticket", jsapi_ticket['jsapi_ticket'], 7000)
        redis.set("wechat:jsapi_ticket_expires_at",
                  jsapi_ticket['jsapi_ticket_expires_at'], 7000)

    return wechat


def wechat_response(data):
    """微信消息处理回复"""
    global message, openid, wechat

    wechat = init_wechat_sdk()
    wechat.parse_data(data)
    message = wechat.get_message()
    openid = message.source
    # 用户信息写入数据库
    set_user_info(openid)

    try:
        get_resp_func = msg_type_response[message.type]
        response = get_resp_func()
    except KeyError:
        # 默认回复微信消息
        response = 'success'

    # 保存最后一次交互的时间
    set_user_last_interact_time(openid, message.time)
    return response


# 储存微信消息类型所对应函数（方法）的字典
msg_type_response = {}


def set_msg_type(msg_type):
    """
    储存微信消息类型所对应函数（方法）的装饰器
    """
    def decorator(func):
        msg_type_response[msg_type] = func
        return func
    return decorator


@set_msg_type('text')
def text_response():
    """文本类型回复"""
    # 默认回复微信消息
    response = 'success'
    # 替换全角空格为半角空格
    message.content = message.content.replace(u'　', ' ')
    # 清除行首空格
    message.content = message.content.lstrip()

    app.logger.warning(u"回复消息: %s" % response)

    return wechat.response_text(response)


@set_msg_type('image')
@set_msg_type('voice')
@set_msg_type('video')
@set_msg_type('music')
@set_msg_type('news')
def image_response():
    response = config.DEFAULT_RESPONSE_TEXT

    return wechat.response_text(response)