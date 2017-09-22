#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine


###系统相关配置####################################################################
DEBUG = False

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'autumn'
MYSQL_PASSWORD = 'autumn'
MYSQL_CHARSET = 'utf8'
MYSQL_DATABASE = 'autumndb'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = 'redispass@$*^$^'

SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{host}/{database}?charset={charset}" .format(
    user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, database=MYSQL_DATABASE, charset=MYSQL_CHARSET)
SQLALCHEMY_DATABASE_ENGINE = create_engine(SQLALCHEMY_DATABASE_URI)
CELERY_BROKER_URL = 'redis://{password}:{host}:{port}/0' .format(
    password=REDIS_PASSWORD, host=REDIS_HOST, port=REDIS_PORT)
CELERY_RESULT_BACKEND = 'redis://{password}:{host}:{port}/1' .format(
    password=REDIS_PASSWORD, host=REDIS_HOST, port=REDIS_PORT)
CELERY_TIMEZONE = 'Asia/Shanghai'

###微信公众平台配置####################################################################
APP_ID = "wx8a0a0bc4b5489057"
APP_SECRET = "50b8b8b835a6c9777e939775006859e0"
TOKEN = "fsdhk23983ghjfdslklfd"
EncodingAESKey = ""

###微信公众平台回复消息#############################################################
DEFAULT_RESPONSE_TEXT = u"请回复正确的文字股票代码获取下个交易日股票涨跌信息，如回复股票代码：000001，" \
                        u"将收到系统回复\"你好，你关注的股票000001(平安银行)，下个交易日呈现上涨(下跌)趋势。\""


###股票相关配置####################################################################
# 股票代码
TRADING_CODE = '600642'
# 上海交易所代码
SH_EXCHANGECODE = 101
# 上海交易所经纬度
SH_LONG = '121e32'
SH_LAT = '31n13'
# 深圳交易所经纬度
SZ_LONG = '114e02'
SZ_LAT = '22n31'

###星盘相关配置####################################################################
# 本命行星列表
LIFE_OBJECTS = [
    'life_sun',
    'life_moon',
    'life_mercury',
    'life_venus',
    'life_mars',
    'life_jupiter',
    'life_saturn',
    # 'life_uranus',
    # 'life_neptune',
    # 'life_pluto'
]

# 本命行星字典
LIFE_OBJECTS_VALUES = {
    'Sun': 'life_sun',
    'Moon': 'life_moon',
    'Mercury': 'life_mercury',
    'Venus': 'life_venus',
    'Mars': 'life_mars',
    'Jupiter': 'life_jupiter',
    'Saturn': 'life_saturn',
    'Uranus': 'life_uranus',
    'Neptune': 'life_neptune',
    'Pluto': 'life_pluto'
}

# 流年行星字典
TRANSIT_OBJECTS_VALUES = {
    'Sun': 'transit_sun',
    'Moon': 'transit_moon',
    'Mercury': 'transit_mercury',
    'Venus': 'transit_venus',
    'Mars': 'transit_mars',
    'Jupiter': 'transit_jupiter',
    'Saturn': 'transit_saturn',
    'Uranus': 'transit_uranus',
    'Neptune': 'transit_neptune',
    'Pluto': 'transit_pluto'
}

# 流年行星列表
TRANSIT_OBJECTS = [
    'transit_sun',
    'transit_moon',
    'transit_mercury',
    'transit_venus',
    'transit_mars',
    'transit_jupiter',
    'transit_saturn',
    'transit_uranus',
    'transit_neptune',
    'transit_pluto'
]

# 行星
SUN = 'Sun'
MOON = 'Moon'
MERCURY = 'Mercury'
VENUS = 'Venus'
MARS = 'Mars'
JUPITER = 'Jupiter'
SATURN = 'Saturn'
URANUS = 'Uranus'
NEPTUNE = 'Neptune'
PLUTO = 'Pluto'

# 所有行星列表
ALL_OBJECTS = [
    'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn',
    'Uranus', 'Neptune', 'Pluto'
]

# 相位
MAJOR_ASPECTS = [0, 60, 90, 120, 180]
MINOR_ASPECTS = [30, 36, 45, 72, 108, 135, 144, 150]
ALL_ASPECTS = MAJOR_ASPECTS + MINOR_ASPECTS

# 默认上市时间
DEFAULT_LISTING_TIME_HOUR = 9
DEFAULT_LISTING_TIME_MINUTE = 30

# 流年使用时间
TRANSIT_DEFAULT_TIME_HOUR = 12
TRANSIT_DEFAULT_TIME_MINUTE = 00
