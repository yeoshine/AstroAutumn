#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..models.stk_basic_info import StkBasicInfo
from ..models.tu_stk_daily_quote import TuStkDailyQuote
import tushare as ts
from instance import config
from ..utils.astro_chart import AstroChart
from ..utils.astro_aspect import AstroAspect
import sys, urllib3, json ,re
from app import redis


class AstroStockService:

    @staticmethod
    def get_stock_info(trading_code=config.TRADING_CODE):
        """获取股票信息"""
        stock_info = StkBasicInfo.query.filter_by(
            TradingCode=trading_code).first()
        return stock_info


    @staticmethod
    def get_daily_quote(trading_code=config.TRADING_CODE):
        """
        获取日线数据写入表
        :param trading_code:
        :return:
        """
        try:
            start = AstroStockService.get_stock_info().ListingDate
            df = ts.get_h_data(trading_code, start=str(start), retry_count=10)
            return df.to_sql(
                'tus_stk_daily_quote',
                config.SQLALCHEMY_DATABASE_ENGINE,
                schema='autumndb',
                if_exists='append')
        except Exception as e:
            return "Class: %s method: %s %s " % (
                AstroStockService.__class__, sys._getframe().f_code.co_name, e)

    @staticmethod
    def get_column_name():
        """
        获取流年vs本命表字段名
        :return:
        """
        try:
            column_list = []
            for a in range(len(config.LIFE_OBJECTS)):
                for b in range(len(config.TRANSIT_OBJECTS)):
                    column_list.append(
                        config.TRANSIT_OBJECTS[b] +
                        '_' +
                        'vs' +
                        '_' +
                        config.LIFE_OBJECTS[a])
            string = ''
            for column in range(len(column_list)):
                string += (
                    "`{column}` int(10) DEFAULT NULL," .format(
                        column=column_list[column]))
            return string
        except Exception as e:
            return "Class: %s method: %s %s " % (
                AstroStockService.__class__, sys._getframe().f_code.co_name, e)

    @staticmethod
    def transit_vs_life(trading_code=config.TRADING_CODE):
        """
        计算流年vs本命相位入库
        :param trading_code:
        :return:
        """
        try:
            stock_info = AstroStockService.get_stock_info(trading_code)
            listing_date = stock_info.ListingDate
            if stock_info.ExchangeCode == config.SH_EXCHANGECODE:
                lat = config.SH_LAT
                long = config.SH_LONG
            else:
                lat = config.SZ_LAT
                long = config.SZ_LONG
            life_chart = AstroChart.handle(
                listing_date.year,
                listing_date.month,
                listing_date.day,
                config.DEFAULT_LISTING_TIME_HOUR,
                config.DEFAULT_LISTING_TIME_MINUTE,
                lat,
                long)
            daily_quote = TuStkDailyQuote.query.filter_by(
                code=trading_code).all()
            for i in range(len(daily_quote)):
                trading_date = daily_quote[i].date
                transit_chart = AstroChart.handle(
                    trading_date.year,
                    trading_date.month,
                    trading_date.day,
                    config.TRANSIT_DEFAULT_TIME_HOUR,
                    config.TRANSIT_DEFAULT_TIME_MINUTE,
                    lat,
                    long)
                aspect_dict = AstroAspect.transit_vs_life_aspect(
                    transit_chart, life_chart)

                sql = "INSERT INTO astro_transit_vs_life (trading_code, trading_date) VALUES ({trading_code}, '{trading_date}')" .format(
                    trading_code=trading_code, trading_date=trading_date)
                config.SQLALCHEMY_DATABASE_ENGINE.execute(sql)
                for key in aspect_dict:
                    up_sql = "UPDATE astro_transit_vs_life set {key} = {values} WHERE trading_code = {trading_code} and trading_date = '{trading_date}'" .format(
                        key=key, values=aspect_dict[key], trading_code=trading_code, trading_date=trading_date)
                    config.SQLALCHEMY_DATABASE_ENGINE.execute(up_sql)
            return True
        except Exception as e:
            return "Class: %s method: %s %s " % (
                AstroStockService.__class__, sys._getframe().f_code.co_name, e)

    @staticmethod
    def get_aspect_count(condition):
        """
        计算给定条件下，流年vs本命相位出现次数入库
        :return:
        """
        try:
            column_list = []
            for a in range(len(config.LIFE_OBJECTS)):
                for b in range(len(config.TRANSIT_OBJECTS)):
                    column_list.append(
                        config.TRANSIT_OBJECTS[b] +
                        '_' +
                        'vs' +
                        '_' +
                        config.LIFE_OBJECTS[a])

            for i in range(len(column_list)):
                column = column_list[i]
                for j in range(len(config.ALL_ASPECTS)):
                    aspect = config.ALL_ASPECTS[j]
                    sql = "select count(*) from `astro_transit_vs_life` a left join `tu_stk_daily_quote` b " \
                          "on a.`trading_code` = b.`code` and a.`trading_date` = b.`date` where " \
                          "b.{where} and a.{column} = {aspect}" .format(where=condition, column=column, aspect=aspect)
                    result = config.SQLALCHEMY_DATABASE_ENGINE.execute(sql)
                    count = result.fetchone()[0]
                    insert_sql = "INSERT INTO `astro_aspect_count` (`condition`, transit_vs_life, aspect, `count`, code) VALUES " \
                        "('{condition}', '{transit_vs_life}', {aspect}, {count}, {code})" \
                        .format(condition=condition, transit_vs_life=column, aspect=aspect, count=count, code=config.TRADING_CODE)
                    config.SQLALCHEMY_DATABASE_ENGINE.execute(insert_sql)
            return True
        except Exception as e:
            return "Class: %s method: %s %s " % (
                AstroStockService.__class__, sys._getframe().f_code.co_name, e)

    @staticmethod
    def get_all_code():
        try:
            host = "www.ctxalgo.com"
            url = "http://www.ctxalgo.com/api/stocks"
            http_pool = urllib3.HTTPConnectionPool(host)
            r = http_pool.urlopen('GET', url)
            data_dict = json.loads(r.data)
            for k,v in data_dict.items():
                code = k
                name = v
                rcode = re.sub('[shsz]', '', code)
                if AstroStockService.return_stock_name(rcode) is None:
                    AstroStockService.save_stock_name(rcode, name)
            sys.exit()
        except Exception as e:
            return "Class: %s method: %s %s " % (
                AstroStockService.__class__, sys._getframe().f_code.co_name, e)


    @staticmethod
    def save_stock_name(code, name):
        redis_prefix = "stock:code:"
        redis.set(redis_prefix + code, name)


    @staticmethod
    def return_stock_name(code):
        redis_prefix = "stock:code:"
        return redis.get(redis_prefix + code)

