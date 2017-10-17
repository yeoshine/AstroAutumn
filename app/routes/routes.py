#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from ..service.wechat_service import *
from flask import request, abort
from ..service.astro_stock_service import AstroStockService
import sys


@app.route("/", methods=['GET', 'POST'])
@check_signature
def handle_wechat_request():
    """
    处理回复微信请求
    """
    if request.method == 'POST':
        try:
            return wechat_response(request.data)
        except Exception as e:
            error =  "method: %s %s " % (sys._getframe().f_code.co_name, e)
            app.logger.warning(u"index error: %s" % error)
    else:
        # 微信接入验证
        return request.args.get('echostr', '')

@app.route("/list", methods=['GET'])
def list():
    return render_template('list.html', name='xxx')


@app.route("/detail", methods=['GET'])
def detail():

    return render_template('detail.html', name='xxx')


@app.route("/menu", methods=['GET'])
def menu():
    return update_menu_setting()


@app.route("/all_stock", methods=['GET'])
def test():
    try:
        code_list =  AstroStockService.all_code()
        for i in range(len(code_list)):
            code = code_list[i]
            name = return_stock_code(code)
            if name:
                # 判断是否有过卜卦记录
                cache_day = trade_day()
                key = config.REDIS_ASTRO_DIVINATION_NAMESPACE + cache_day + ':' + code
                redis_message = redis.hget(key, 'message')
                if not redis_message:
                    result = AstroDivination.handle(str(code), str(name.decode()))
                    redis.hmset(key,
                                {"openid": 'local',
                                 "code": code,
                                 "name": name,
                                 "score": result['score'],
                                 "performance": result['performance'],
                                 "message": result['message'],
                                 "divination_time": result['divination_time'],
                                 "divination_times": 1,
                                 "message_time": time.strftime("%Y-%m-%d %H:%M:%S",
                                                               time.localtime())})
                else:
                    redis.hincrby(key, 'divination_times', 1)
    except Exception as e:
        return e









