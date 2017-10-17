#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.service.astro_stock_service import AstroStockService
from app.service.wechat_service import *
import sys


class DivinationData:

    @staticmethod
    def all_stock_result():
        try:
            code_list =  AstroStockService.all_code()
            for i in range(len(code_list)):
                code = code_list[i]
                name = return_stock_code(code)
                if name:
                    # 判断是否有过卜卦记录
                    cache_day = trade_day()
                    key = config.REDIS_ASTRO_DIVINATION_NAMESPACE + cache_day + ':' + code
                    redis_message = redis.hget(key, 'message')
                    if not redis_message:
                        result = AstroDivination.handle(str(code), str(name.decode()))
                        redis.hmset(key,
                                    {"openid": 'local',
                                     "code": code,
                                     "name": name,
                                     "score": result['score'],
                                     "performance": result['performance'],
                                     "message": result['message'],
                                     "divination_time": result['divination_time'],
                                     "divination_times": 1,
                                     "message_time": time.strftime("%Y-%m-%d %H:%M:%S",
                                                                   time.localtime())})
                    else:
                        redis.hincrby(key, 'divination_times', 1)
        except Exception as e:
            return e


    @staticmethod
    def divination_result():
        all = 0
        correct = 0
        wrong = 0
        try:
            code_list = AstroStockService.all_code()
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
                    print(today)
                    sys.exit()
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
    x = DivinationData.divination_result()
    print(x)
