#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db

class TuStkDailyQuote(db.Model):
    __tablename__ = 'tu_stk_daily_quote'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20))
    date = db.Column(db.Date)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    close = db.Column(db.Float)
    low = db.Column(db.Float)
    volume = db.Column(db.Float)
    p_change = db.Column(db.Float)