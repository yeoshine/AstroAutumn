#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db

class AstroDivinationResult(db.Model):
    __tablename__ = 'astro_divination_result'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    all_number = db.Column(db.Integer)
    correct_number = db.Column(db.Integer)
    wrong_number = db.Column(db.Integer)
    correct_code = db.Column(db.TEXT)
    wrong_code = db.Column(db.TEXT)
    divination_time = db.Column(db.DATE)
    result_time = db.Column(db.DATE)
    accuracy = db.Column(db.Integer)
    updated_at = db.Column(db.DATETIME)
    created_at = db.Column(db.DATETIME)