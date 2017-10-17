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



@app.route("/test", methods=['GET'])
def test_get():
    pass
    # import tushare as ts
    # df = ts.get_hist_data('000001', start='2017-10-17', end='2017-10-17')
    # from ..utils import autumn_date
    # yesterday = autumn_date.get_yesterday()








