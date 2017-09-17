#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import app
from ..service.stk_basic_info_service import StkBasicInfoService

@app.route("/", methods=['GET', 'POST'])
def index():
    return StkBasicInfoService.get_aspect_count()

#
# @app.route("/get_column_name", methods=['GET', 'POST'])
# def index():
#     return StkBasicInfoService.get_column_name()