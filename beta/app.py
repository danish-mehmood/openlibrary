#!/usr/bin/env pythonNone
#-*-coding: utf-8 -*-

"""
    app.py
    ~~~~~~


    :copyright: (c) 2016 by Anonymous
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask
from flask.ext.routing import router
import views
from configs import options

urls = (
    '/partials/<path:partial>', views.Partial,
    '/books/<path:id>', views.WorkEdition,
    '/', views.Base
)
app = router(Flask(__name__), urls)

if __name__ == "__main__":
    app.run(**options)
