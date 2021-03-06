#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db

class AstroTransitVsLife(db.Model):
    __tablename__ = 'astro_transit_vs_life'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trading_code = db.Column(db.Integer)
    trading_date = db.Column(db.Date)
    transit_sun_vs_life_sun = db.Column(db.Integer)
    transit_moon_vs_life_sun = db.Column(db.Integer)
    transit_mercury_vs_life_sun = db.Column(db.Integer)
    transit_venus_vs_life_sun = db.Column(db.Integer)
    transit_mars_vs_life_sun = db.Column(db.Integer)
    transit_jupiter_vs_life_sun = db.Column(db.Integer)
    transit_saturn_vs_life_sun = db.Column(db.Integer)
    transit_uranus_vs_life_sun = db.Column(db.Integer)
    transit_neptune_vs_life_sun = db.Column(db.Integer)
    transit_pluto_vs_life_sun = db.Column(db.Integer)
    transit_sun_vs_life_moon = db.Column(db.Integer)
    transit_moon_vs_life_moon = db.Column(db.Integer)
    transit_mercury_vs_life_moon = db.Column(db.Integer)
    transit_venus_vs_life_moon = db.Column(db.Integer)
    transit_mars_vs_life_moon = db.Column(db.Integer)
    transit_jupiter_vs_life_moon = db.Column(db.Integer)
    transit_saturn_vs_life_moon = db.Column(db.Integer)
    transit_uranus_vs_life_moon = db.Column(db.Integer)
    transit_neptune_vs_life_moon = db.Column(db.Integer)
    transit_pluto_vs_life_moon = db.Column(db.Integer)
    transit_sun_vs_life_mercury = db.Column(db.Integer)
    transit_moon_vs_life_mercury = db.Column(db.Integer)
    transit_mercury_vs_life_mercury = db.Column(db.Integer)
    transit_venus_vs_life_mercury = db.Column(db.Integer)
    transit_mars_vs_life_mercury = db.Column(db.Integer)
    transit_jupiter_vs_life_mercury = db.Column(db.Integer)
    transit_saturn_vs_life_mercury = db.Column(db.Integer)
    transit_uranus_vs_life_mercury = db.Column(db.Integer)
    transit_neptune_vs_life_mercury = db.Column(db.Integer)
    transit_pluto_vs_life_mercury = db.Column(db.Integer)
    transit_sun_vs_life_venus = db.Column(db.Integer)
    transit_moon_vs_life_venus = db.Column(db.Integer)
    transit_mercury_vs_life_venus = db.Column(db.Integer)
    transit_venus_vs_life_venus = db.Column(db.Integer)
    transit_mars_vs_life_venus = db.Column(db.Integer)
    transit_jupiter_vs_life_venus = db.Column(db.Integer)
    transit_saturn_vs_life_venus = db.Column(db.Integer)
    transit_uranus_vs_life_venus = db.Column(db.Integer)
    transit_neptune_vs_life_venus = db.Column(db.Integer)
    transit_pluto_vs_life_venus = db.Column(db.Integer)
    transit_sun_vs_life_mars = db.Column(db.Integer)
    transit_moon_vs_life_mars = db.Column(db.Integer)
    transit_mercury_vs_life_mars = db.Column(db.Integer)
    transit_venus_vs_life_mars = db.Column(db.Integer)
    transit_mars_vs_life_mars = db.Column(db.Integer)
    transit_jupiter_vs_life_mars = db.Column(db.Integer)
    transit_saturn_vs_life_mars = db.Column(db.Integer)
    transit_uranus_vs_life_mars = db.Column(db.Integer)
    transit_neptune_vs_life_mars = db.Column(db.Integer)
    transit_pluto_vs_life_mars = db.Column(db.Integer)
    transit_sun_vs_life_jupiter = db.Column(db.Integer)
    transit_moon_vs_life_jupiter = db.Column(db.Integer)
    transit_mercury_vs_life_jupiter = db.Column(db.Integer)
    transit_venus_vs_life_jupiter = db.Column(db.Integer)
    transit_mars_vs_life_jupiter = db.Column(db.Integer)
    transit_jupiter_vs_life_jupiter = db.Column(db.Integer)
    transit_saturn_vs_life_jupiter = db.Column(db.Integer)
    transit_uranus_vs_life_jupiter = db.Column(db.Integer)
    transit_neptune_vs_life_jupiter = db.Column(db.Integer)
    transit_pluto_vs_life_jupiter = db.Column(db.Integer)
    transit_sun_vs_life_saturn = db.Column(db.Integer)
    transit_moon_vs_life_saturn = db.Column(db.Integer)
    transit_mercury_vs_life_saturn = db.Column(db.Integer)
    transit_venus_vs_life_saturn = db.Column(db.Integer)
    transit_mars_vs_life_saturn = db.Column(db.Integer)
    transit_jupiter_vs_life_saturn = db.Column(db.Integer)
    transit_saturn_vs_life_saturn = db.Column(db.Integer)
    transit_uranus_vs_life_saturn = db.Column(db.Integer)
    transit_neptune_vs_life_saturn = db.Column(db.Integer)
    transit_pluto_vs_life_saturn = db.Column(db.Integer)
    transit_sun_vs_life_uranus = db.Column(db.Integer)
    transit_moon_vs_life_uranus = db.Column(db.Integer)
    transit_mercury_vs_life_uranus = db.Column(db.Integer)
    transit_venus_vs_life_uranus = db.Column(db.Integer)
    transit_mars_vs_life_uranus = db.Column(db.Integer)
    transit_jupiter_vs_life_uranus = db.Column(db.Integer)
    transit_saturn_vs_life_uranus = db.Column(db.Integer)
    transit_uranus_vs_life_uranus = db.Column(db.Integer)
    transit_neptune_vs_life_uranus = db.Column(db.Integer)
    transit_pluto_vs_life_uranus = db.Column(db.Integer)
    transit_sun_vs_life_neptune = db.Column(db.Integer)
    transit_moon_vs_life_neptune = db.Column(db.Integer)
    transit_mercury_vs_life_neptune = db.Column(db.Integer)
    transit_venus_vs_life_neptune = db.Column(db.Integer)
    transit_mars_vs_life_neptune = db.Column(db.Integer)
    transit_jupiter_vs_life_neptune = db.Column(db.Integer)
    transit_saturn_vs_life_neptune = db.Column(db.Integer)
    transit_uranus_vs_life_neptune = db.Column(db.Integer)
    transit_neptune_vs_life_neptune = db.Column(db.Integer)
    transit_pluto_vs_life_neptune = db.Column(db.Integer)
    transit_sun_vs_life_pluto = db.Column(db.Integer)
    transit_moon_vs_life_pluto = db.Column(db.Integer)
    transit_mercury_vs_life_pluto = db.Column(db.Integer)
    transit_venus_vs_life_pluto = db.Column(db.Integer)
    transit_mars_vs_life_pluto = db.Column(db.Integer)
    transit_jupiter_vs_life_pluto = db.Column(db.Integer)
    transit_saturn_vs_life_pluto = db.Column(db.Integer)
    transit_uranus_vs_life_pluto = db.Column(db.Integer)
    transit_neptune_vs_life_pluto = db.Column(db.Integer)
    transit_pluto_vs_life_pluto = db.Column(db.Integer)


    def save(self):
        db.session.add(self)
        db.session.commit()
        return self