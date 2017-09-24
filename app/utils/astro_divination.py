#!/usr/bin/env python
# -*- coding: utf-8 -*-
import radar
import datetime
from .astro_chart import AstroChart
from .astro_aspect import AstroAspect
from instance import config

# 卜卦计算类


class AstroDivination:

    # 卜卦起止时间
    DEFAULT_RANDOM_START_TIME = '1900-01-01T00:00:00'
    DEFAULT_RANDOM_END_TIME = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    # 卜卦默认经纬度北京
    DEFAULT_DIVINATION_LONG = "116e28"
    DEFAULT_DIVINATION_LAT = "39n54"

    @staticmethod
    def create_divination_time():
        """
        创建卜卦时间
        :return:
        """
        return radar.random_datetime(
            start=AstroDivination.DEFAULT_RANDOM_START_TIME,
            stop=AstroDivination.DEFAULT_RANDOM_END_TIME)

    @staticmethod
    def create_divination_chart():
        """
        创建卜卦盘
        :return:
        """
        divination_time = AstroDivination.create_divination_time()
        chart = AstroChart.handle(
            divination_time.year,
            divination_time.month,
            divination_time.day,
            divination_time.hour,
            divination_time.minute,
            AstroDivination.DEFAULT_DIVINATION_LAT,
            AstroDivination.DEFAULT_DIVINATION_LONG)
        return chart

    @staticmethod
    def divination_score():
        """
        计算卜卦盘分数
        :return:
        """
        divination_chart = AstroDivination.create_divination_chart()
        divination_object_score_dict = AstroDivination.divination_object_score(divination_chart)
        return AstroDivination.divination_aspect_score(divination_chart, divination_object_score_dict)



    @staticmethod
    def divination_aspect_score(divination_chart, divination_object_score_dict):
        """
        计算卜卦盘相位分数
        :param divination_chart:
        :return:
        """
        aspect_list = AstroAspect.divination_aspect(divination_chart)
        score = 0
        for i in range(len(aspect_list)):
            object1 = aspect_list[i].active.id
            object2 = aspect_list[i].passive.id
            aspect = aspect_list[i].type
            if aspect != -1:
                if object1 in divination_object_score_dict:
                    score += divination_object_score_dict[object1] + \
                         config.DIVINATION_ASPECT_SCORE[aspect] + divination_object_score_dict[object2]
        return score


    @staticmethod
    def divination_object_score(divination_chart):
        """
        卜卦盘行星分数重算,返回只需要的行星和分数
        :param divination_chart:
        :return:
        """

        # 各宫落在的星座
        house1_sign = divination_chart.houses.content['House1'].sign
        house5_sign = divination_chart.houses.content['House5'].sign
        house11_sign = divination_chart.houses.content['House11'].sign
        house8_sign = divination_chart.houses.content['House8'].sign

        # 星座守护星
        house1_object = config.SIGN_RULER[house1_sign]
        house5_object = config.SIGN_RULER[house5_sign]
        house11_object = config.SIGN_RULER[house11_sign]
        house8_object = config.SIGN_RULER[house8_sign]

        divination_objects_score = {}
        for k, v in config.OBJECTS_SCORE.items():
            score = 0
            if k == house1_object:
                score += v * config.DIVINATION_ASC_SIGN_RULER_WEIGHT
            if k == 'Sun':
                score += v * config.DIVINATION_SUN_WEIGHT
            if k == 'Moon':
                score += v * config.DIVINATION_MOON_WEIGHT
            if k == house5_object:
                score += v * config.DIVINATION_5HOUSE_WEIGHT
            if k == house11_object:
                score += v * config.DIVINATION_11HOUSE_WEIGHT
            if k == house8_object:
                score += v * config.DIVINATION_8HOUSE_WEIGHT
            divination_objects_score.setdefault(k, score)

        #剔除没加分行星,只考虑分数已经变化行星相位
        for k1, v1 in divination_objects_score.items():
            for k2, v2 in config.OBJECTS_SCORE.items():
                if k1 == k2 and v1 == v2:
                    del divination_objects_score[k1]

        return divination_objects_score










