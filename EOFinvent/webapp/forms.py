#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:24:40 2018

@author: danw
"""

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired

from wtforms.fields.html5 import DateField

class AddForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    assettag = IntegerField("asset tag", validators=[DataRequired()])
    serial = StringField("serial number")
    
    
    acquired = DateField("Date acquired", validators=[DataRequired()], 
                        format="%d-%m-%Y")
    
    
    submit = SubmitField(label="submit")
    