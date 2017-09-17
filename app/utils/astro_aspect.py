# -*- coding:utf-8 -*-

from flatlib.aspects import *
from instance import config

class AstroAspect:
    # chart = AstroChart.handle(1984, 5, 29, 23, 40, '39n54', '116e28')
    #
    # asc = chart.get(const.ASC)
    # desc = chart.get(const.DESC)
    # mc = chart.get(const.MC)
    # ic = chart.get(const.IC)
    #
    # sun = chart.get(const.SUN)
    # venus = chart.get(const.VENUS)
    # mecury = chart.get(const.MERCURY)
    # mars = chart.get(const.MARS)
    #
    # sun_venus_aspect = getAspect(sun, venus, const.MAJOR_ASPECTS).type
    # mecury_mars_aspect = getAspect(mecury, mars, const.MAJOR_ASPECTS).type
    #
    # transit_chart = AstroChart.handle(2017, 9, 14, 19, 15, '39n54', '116e28')
    # transit_mars = transit_chart.get(const.MARS)
    # transit_sun = transit_chart.get(const.SUN)
    #
    # transit_mars_venus_aspect = getAspect(transit_mars, venus, const.MAJOR_ASPECTS)
    # a = getAspect(transit_sun, venus, const.MAJOR_ASPECTS)
    #
    # transit_chart.get(const.NEPTUNE)


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