#!/usr/bin/python3
# PLD Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base

engine = create_engine('sqlite:///orm.db')
connection = engine.connect()

