#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.service.astro_stock_service import AstroStockService
from app.service.wechat_service import *
from app.utils import autumn_date
from app.models.astro_divination_result import AstroDivinationResult


class DivinationData:

    @staticmethod
    def all_stock_result():
        try:
            code_list = AstroStockService.all_code()
            for i in range(len(code_list)):
                code = code_list[i]
                name = return_stock_code(code)
                if name:
                    # 判断是否有过卜卦记录
                    cache_day = trade_day()
                    key = config.REDIS_ASTRO_DIVINATION_NAMESPACE + cache_day + ':' + code
                    redis_message = redis.hget(key, 'message')
                    if not redis_message:
                        result = AstroDivination.handle(
                            str(code), str(name.decode()))
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
        all_number = 0
        correct_number = 0
        correct_code = []
        wrong_number = 0
        wrong_code = []
        today = autumn_date.get_today().strftime('%Y-%m-%d')
        yesterday = autumn_date.get_yesterday().strftime('%Y%m%d')
        try:
            code_list = AstroStockService.all_code()
            for i in range(len(code_list)):
                code = '000100'
                yesterday = '20171017'
                key = config.REDIS_ASTRO_DIVINATION_NAMESPACE + yesterday + ':' + code
                performance = redis.hget(key, 'performance').decode()
                if performance is '1' or performance is '0':
                    all_number += 1
                    import tushare as ts
                    df = ts.get_hist_data(code, start=today, end=today)
                    if df.p_change.values[0]:
                        if df.p_change.values[0] > 0 and performance is '1':
                            correct_number += 1
                            correct_code.append(code)
                        if df.p_change.values[0] > 0 and performance is '0':
                            wrong_number += 1
                            wrong_code.append(code)
                        if df.p_change.values[0] < 0 and performance is '0':
                            correct_number += 1
                            correct_code.append(code)
                        if df.p_change.values[0] < 0 and performance is '1':
                            wrong_number += 1
                            wrong_code.append(code)
                    else:
                        print('no_df')
                else:
                    print('no_performance')
            correct_code_str = DivinationData.list_to_string(correct_code)
            wrong_code_str = DivinationData.list_to_string(wrong_code)
            dict = {
                'all_number': all_number,
                'correct_number': correct_number,
                'wrong_number': wrong_number,
                'accuracy': correct_number/all_number * 100,
                'correct_code': correct_code_str,
                'wrong_code': wrong_code_str,
                'divination_time': autumn_date.get_yesterday().strftime('%Y-%m-%d'),
                'result_time': today}
            print(dict)
            return AstroDivinationResult(dict).save()
        except Exception as e:
            return e

    @staticmethod
    def list_to_string(list):
        return (",".join(str(i) for i in list))


if __name__ == '__main__':
    DivinationData.divination_result()
