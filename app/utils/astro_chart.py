# -*- coding:utf-8 -*-

from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.aspects import *


class AstroChart:

    MINUTE_DEVIATION = -1
    DEFAULT_SECOND = 48
    UTC = '+08:00'

    @staticmethod
    def handle(year, moon, day, hour, minute, lat, lon):
        date_calcu = AstroChart.date(year, moon, day)
        time_calcu = AstroChart.time(hour, minute)
        date = AstroChart.flat_date(date_calcu, time_calcu)
        position = AstroChart.flat_position(lat, lon)
        return AstroChart.flat_chart(date, position)

    @staticmethod
    def date(year, moon, day):
        return "{year}/{moon}/{day}" .format(year=year, moon=moon, day=day)

    @staticmethod
    def time(hour, minute):
        return "{hour}:{minute}:{second}" .format(
            hour=hour,
            minute=int(
                minute +
                AstroChart.MINUTE_DEVIATION),
            second=AstroChart.DEFAULT_SECOND)

    @staticmethod
    def flat_date(date, time):
        return Datetime(date, time, AstroChart.UTC)

    @staticmethod
    def flat_position(lat, lon):
        return GeoPos(lat, lon)

    @staticmethod
    def flat_chart(date, pos):
        return Chart(date, pos, IDs=const.LIST_OBJECTS)

