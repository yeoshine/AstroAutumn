#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db
from datetime import datetime

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
    updated_at = db.Column(db.DATETIME, default=datetime.now)
    created_at = db.Column(db.DATETIME, default=datetime.now)


    def __init__(self, dict):
        self.all_number = dict['all_number']
        self.correct_number = dict['correct_number']
        self.wrong_number = dict['wrong_number']
        self.correct_code = dict['correct_code']
        self.wrong_code = dict['wrong_code']
        self.divination_time = dict['divination_time']
        self.result_time = dict['result_time']
        self.accuracy = dict['accuracy']

    def save(self):
        db.session.add(self)
        db.session.commit()