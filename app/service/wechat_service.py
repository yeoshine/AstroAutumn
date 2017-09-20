#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wechatpy import parse_message, create_reply
from wechatpy.replies import TextReply
from wechatpy.messages import *
from .. import app


class WechatService:

    @staticmethod
    def message(data):
        msg = parse_message(data)
        if msg.type == 'text':
            app.logger.warning(
                u'FromUserName: {FromUserName}, CreateTime: {CreateTime}, MsgId: {MsgId}, Content：{Content}'.format(
                    FromUserName=msg.source,
                    CreateTime=msg.create_time,
                    MsgId=msg.id,
                    Content=msg.content))
            reply = TextReply(content='此功能正在开发中……', message=msg)
        else:
            reply = create_reply('此功能正在开发中……', msg)
        return reply.render()
