#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import logging
from redis import Redis
from logging.handlers import RotatingFileHandler


app = Flask(__name__, instance_relative_config=True)
# 加载配置
# app.config.from_object('config')
app.config.from_pyfile('config.py')


# 记录日志
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

redis = Redis()
