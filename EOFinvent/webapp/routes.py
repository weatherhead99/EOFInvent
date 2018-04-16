#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:33:50 2018

@author: danw
"""

from flask import render_template
from webapp import webapp

@webapp.route('/')
@webapp.route('/index')
def index():
    return render_template("index.html")
