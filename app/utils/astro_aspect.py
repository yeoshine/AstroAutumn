# -*- coding:utf-8 -*-

from flatlib.aspects import *
from instance import config

class AstroAspect:

    @staticmethod
    def transit_vs_life_aspect(transit_chart, life_chart):
        """
        计算流年vs本命行星角度
        :param transit_chart:
        :param life_chart:
        :return:
        """
        life_object_list = []
        for a in range(len(config.ALL_OBJECTS)):
            life_object_list.append(life_chart.get(config.ALL_OBJECTS[a]))

        transit_object_list = []
        for b in range(len(config.ALL_OBJECTS)):
            transit_object_list.append(transit_chart.get(config.ALL_OBJECTS[b]))

        transit_vs_life_list = []
        for y in range(len(transit_object_list)):
            for z in range(len(life_object_list)):
                aspect = getAspect(transit_object_list[y], life_object_list[z], config.ALL_ASPECTS)
                transit_vs_life_list.append(aspect)

        final_dic = {}
        for i in range(len(transit_vs_life_list)):
            transit = transit_vs_life_list[i].active.id
            life = transit_vs_life_list[i].passive.id
            aspect = transit_vs_life_list[i].type
            if aspect != -1:
                string = config.TRANSIT_OBJECTS_VALUES[str(transit)] + '_' + 'vs' + '_' + config.LIFE_OBJECTS_VALUES[str(life)]
                final_dic.setdefault(string, aspect)

        return final_dic


    @staticmethod
    def divination_aspect(divination_chart):
        """
        计算卜卦盘行星相位，返回相位列表
        :param divination_chart:
        :return:
        """
        object_list_a = []
        for a in range(len(config.DIVINATION_OBJECTS)):
            object_list_a.append(divination_chart.get(config.DIVINATION_OBJECTS[a]))

        object_list_b = object_list_a

        aspect_list = []
        for x in range(len(object_list_a)):
            for y in range(len(object_list_b)):
                aspect = getAspect(object_list_a[x], object_list_b[y], config.MAJOR_ASPECTS)
                aspect_list.append(aspect)

        return aspect_list