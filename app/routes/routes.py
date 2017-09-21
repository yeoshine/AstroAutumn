#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app
from ..service.wechat_service import *
from flask import request, abort


@app.route("/", methods=['GET', 'POST'])
@check_signature
def handle_wechat_request():
    """
    处理回复微信请求
    """
    if request.method == 'POST':
        return wechat_response(request.data)
    else:
        # 微信接入验证
        return request.args.get('echostr', '')