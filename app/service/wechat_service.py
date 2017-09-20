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
            app.logger.warning(u'FromUserName: {FromUserName}, ' .format(FromUserName=msg.content))
            reply=TextReply(content='text reply', message=msg)
        else:
            reply=create_reply('Sorry, can not handle this for now', msg)
        return reply.render()
