#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db

class StkBasicInfo(db.Model):
    __tablename__ = 'stk_basic_info'

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ComCode = db.Column(db.Integer)
    TradingCode = db.Column(db.String(10))
    SecuAbbr = db.Column(db.String(50))
    ChiName = db.Column(db.String(200))
    ChiNameAbbr = db.Column(db.String(100))
    ChiSpelling = db.Column(db.String(20))
    EngName = db.Column(db.String(200))
    EngNameAbbr = db.Column(db.String(100))
    SecuCategory = db.Column(db.String(100))
    ExchangeCode = db.Column(db.Integer)
    ExchangeName = db.Column(db.String(100))
    ListingDate = db.Column(db.Date)
    DelistingDate = db.Column(db.Date)
    BoardCode = db.Column(db.Integer)
    BoardName = db.Column(db.String(200))

    def __repr__(self):
        return '<ListingDate=%s>' % (self.ListingDate)