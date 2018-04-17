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

PROVENANCE_DESCRIPTIONS = {
        Provenance.Purchased : "Purchased",
        Provenance.Donated : "Donated",
        Provenance.LongTermLoan : "Long Term Loan",
        Provenance.ShortTermLoan : "Short Term Loan"
        }



class Status(enum.Enum):
    Operating = 1
    Broken = 2
    
STATUS_DESCRIPTIONS = {
        Status.Operating : "Working",
        Status.Broken : "Broken"
}
    
class Training(enum.Enum):
    NotRequired = 1
    Induction = 2
    Specific = 3

TRAINING_DESCRIPTIONS = {
        Training.NotRequired : "No Training Requried",
        Training.Induction : "Covered In General Induction",
        Training.Specific : "Specific Training Required" 
}


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("userid_seq"), primary_key=True)
    name = Column(String)
    email = Column(String)
    perm_add = Column(Boolean)
    perm_delete_own = Column(Boolean)
    perm_delete_others = Column(Boolean)
    perm_edit_own = Column(Boolean)
    perm_delete_others = Column(Boolean)

class InventoryCategories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class InventoryLocations(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class InventoryItem(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    provenance = Column(Enum(Provenance))
    donothack = Column(Boolean)
    name = Column(String)
    acquired = Column(Date)
    user_responsible = Column(Integer, ForeignKey("users.id"))
    owner = Column(String)
    
    serialno = Column(String)
    manufacturer = Column(String)
    category = Column(Integer, ForeignKey("categories.id"))
    location = Column(Integer, ForeignKey("locations.id"))
    
    sched_maintenance = Column(Date)
    last_maintenance = Column(Date)
    
    notes = Column(String)
    
    user_rel = relationship("User", back_populates="items")
    category_rel = relationship("InventoryCategories", back_populates="items")
    location_rel = relationship("InventoryLocations", back_populates="items")




if __name__ == "__main__":
    engine = create_engine("sqlite:///memory",echo=True)