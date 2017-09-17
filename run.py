#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from app.routes import routes

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run()