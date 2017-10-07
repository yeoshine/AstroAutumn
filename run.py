#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from app.routes import routes

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    # app.run('0.0.0.0', debug=False, port=443, ssl_context='adhoc')
    app.run('0.0.0.0', debug=True)