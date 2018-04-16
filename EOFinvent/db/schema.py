#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:21:15 2018

@author: weatherill
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum

from sqlalchemy import create_engine
import enum


Base = declarative_base()

class Provenance(enum.Enum):
    Purchased = 1
    Donated = 2
    LongTermLoan = 3
    ShortTermLoan = 4


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class InventoryItem(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    provenance = Column(Enum(Provenance))
    





if __name__ == "__main__":
    engine = create_engine("sqlite:///memory",echo=True)