#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:21:15 2018

@author: weatherill
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, Boolean, Sequence, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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
    id = Column(Integer, Sequence("userid_seq"), primary_key=True)
    name = Column(String)
    email = Column(String)

class InventoryCategories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class InventoryLocations(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)


class InventoryItem(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    provenance = Column(Enum(Provenance))
    donothack = Column(Boolean)
    name = Column(String)
    acquired = Column(Date)
    user_responsible = Column(Integer, ForeignKey("users.id"))
    
    category = Column(Integer, ForeignKey("categories.id"))
    location = Column(Integer, ForeignKey("locations.id"))
    
    user_rel = relationship("User", back_populates="items")
    category_rel = relationship("InventoryCategories", back_populates="items")
    location_rel = relationship("InventoryLocations", back_populates="items")




if __name__ == "__main__":
    engine = create_engine("sqlite:///memory",echo=True)