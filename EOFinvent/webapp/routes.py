#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:33:50 2018

@author: danw
"""

from flask import render_template, flash, redirect
from webapp import webapp
from webapp.forms import AddForm


@webapp.route('/')
@webapp.route('/index')
def index():
    return render_template("index.html")

@webapp.route('/add', methods=["GET","POST"])
def add():
    form = AddForm()
    
    if form.validate_on_submit():
        flash("submitted!")
        return redirect("/add")
    
    return render_template("add.html",form=form)