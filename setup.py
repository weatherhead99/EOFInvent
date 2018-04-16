#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:15:43 2018

@author: weatherill
"""

import os
from setuptools import setup, find_packages

setup(
      name="EOFinvent",
      version="0.0.1dev",
      author="Dan Weatherill",
      packages=find_packages(),
      install_requires=[
              "SQLAlchemy"
              ]
      )