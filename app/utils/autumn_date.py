#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime

def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday.strftime('%Y%m%d')

def get_today():
    today = datetime.date.today()
    return today.strftime('%Y-%m-%d')