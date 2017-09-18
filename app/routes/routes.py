#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app
from ..service.astro_stock_service import AstroStockService

@app.route("/", methods=['GET', 'POST'])
def index():
    return AstroStockService.get_aspect_count()

#
# @app.route("/get_column_name", methods=['GET', 'POST'])
# def index():
#     return StkBasicInfoService.get_column_name()