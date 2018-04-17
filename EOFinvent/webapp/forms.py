#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:24:40 2018

@author: danw
"""

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired

from wtforms.fields.html5 import DateField
from datetime import date

from db.schema import PROVENANCE_DESCRIPTIONS


class AddForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    assettag = IntegerField("asset tag", validators=[DataRequired()])
    serial = StringField("serial number")
    
    
    acquired = DateField("Date acquired", validators=[DataRequired()], 
                        format="%d-%m-%Y", default=date.today)

    donothack = BooleanField("Do Not Hack")
    
    
    submit = SubmitField(label="submit")
    