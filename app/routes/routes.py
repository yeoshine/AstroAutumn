#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app
from ..service.astro_stock_service import AstroStockService
from ..service.wechat_service import WechatService
from flask import request, abort
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from instance import config


@app.route("/", methods=['GET', 'POST'])
def index():
    return "index"
    # condition = "p_change > 0"
    # condition = "p_change < 0"
    # insert_transit_vs_life = AstroStockService.transit_vs_life()
    # if insert_transit_vs_life is True:
    #     return AstroStockService.get_aspect_count(condition)
    # return AstroStockService.get_aspect_count(condition)


@app.route("/wechat", methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echo_str = request.args.get('echostr', '')
    try:
        check_signature(config.WECHAT_TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)
    if request.method == 'GET':
        return echo_str
    else:
        return WechatService.message(request.data)