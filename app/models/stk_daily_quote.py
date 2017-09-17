#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db

class StkDailyQuote(db.Model):
    __tablename__ = 'stk_daily_quote'

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trading_code = db.Column(db.String(20))
    trading_date = db.Column(db.Date)
    high = db.Column(db.Float)
    close = db.Column(db.Float)
    low = db.Column(db.Float)
    volume = db.Column(db.Float)
    price_change = db.Column(db.Float)
    p_change = db.Column(db.Float)
    ma5 = db.Column(db.Float)
    ma10 = db.Column(db.Float)
    ma20 = db.Column(db.Float)
    v_ma5 = db.Column(db.Float)
    v_ma10 = db.Column(db.Float)
    v_ma20 = db.Column(db.Float)
    turnover = db.Column(db.Float)
