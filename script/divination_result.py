#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app.service.astro_stock_service import AstroStockService
from ..app.service.wechat_service import *


def divination_result():
    all = 0
    correct = 0
    wrong = 0
    try:
        code_list =  AstroStockService.all_code()
        for i in range(len(code_list)):
            code = code_list[i]
            from app.utils import autumn_date
            yesterday = autumn_date.get_yesterday()
            key = config.REDIS_ASTRO_DIVINATION_NAMESPACE + yesterday + ':' + code
            performance = redis.hget(key, 'performance')
            if performance:
                all += 1
                import tushare as ts
                today = autumn_date.get_today()
                df = ts.get_hist_data(code, start=today, end=today)
                if df.p_change > 0:
                    correct += 1
                else:
                    wrong += 1
        dict = {'all': all, 'correct': correct, 'wrong': wrong}
        return dict
    except Exception as e:
        return e


if __name__ == '__main__':
    divination_result()