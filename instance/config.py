#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine


DEBUG = True

TRADING_CODE = '600642'

SH_EXCHANGECODE = 101

SQLALCHEMY_DATABASE_URI = "mysql://root:000000@127.0.0.1/autumndb?charset=utf8mb4"

SQLALCHEMY_DATABASE_ENGINE = create_engine(SQLALCHEMY_DATABASE_URI)

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

LIFE_OBJECTS_VALUES = {
    'Sun':'life_sun',
    'Moon':'life_moon',
    'Mercury': 'life_mercury',
    'Venus': 'life_venus',
    'Mars': 'life_mars',
    'Jupiter': 'life_jupiter',
    'Saturn': 'life_saturn',
    'Uranus': 'life_uranus',
    'Neptune': 'life_neptune',
    'Pluto': 'life_pluto'
}

TRANSIT_OBJECTS_VALUES = {
    'Sun':'transit_sun',
    'Moon':'transit_moon',
    'Mercury': 'transit_mercury',
    'Venus': 'transit_venus',
    'Mars': 'transit_mars',
    'Jupiter': 'transit_jupiter',
    'Saturn': 'transit_saturn',
    'Uranus': 'transit_uranus',
    'Neptune': 'transit_neptune',
    'Pluto': 'transit_pluto'
}


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

ALL_OBJECTS = [
    'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn',
    'Uranus', 'Neptune', 'Pluto'
]

ASPECT_LIST = [0, 60, 90, 120, 180]

DEFAULT_LISTING_TIME_HOUR = 9
DEFAULT_LISTING_TIME_MINUTE = 30

TRANSIT_DEFAULT_TIME_HOUR = 12
TRANSIT_DEFAULT_TIME_MINUTE = 00


SH_LONG = '121e32'
SH_LAT  = '31n13'

SZ_LONG = '114e02'
SZ_LAT  = '22n31'