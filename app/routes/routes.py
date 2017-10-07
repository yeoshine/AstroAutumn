#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app
from flask import render_template
from ..service.wechat_service import *
from ..service.astro_stock_service import AstroStockService
from flask import request, abort
from ..utils.astro_divination import AstroDivination
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
