# -*- coding:utf-8 -*-

from flatlib.aspects import *
from instance import config

class AstroAspect:

    @staticmethod
    def transit_vs_life_aspect(transit_chart, life_chart):
        life_object_list = []
        for a in range(len(config.ALL_OBJECTS)):
            life_object_list.append(life_chart.get(config.ALL_OBJECTS[a]))

        transit_object_list = []
        for b in range(len(config.ALL_OBJECTS)):
            transit_object_list.append(transit_chart.get(config.ALL_OBJECTS[b]))

        transit_vs_life_list = []
        for y in range(len(transit_object_list)):
            for z in range(len(life_object_list)):
                aspect = getAspect(transit_object_list[y], life_object_list[z], const.MAJOR_ASPECTS)
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