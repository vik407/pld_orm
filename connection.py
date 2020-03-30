#!/usr/bin/python3
# PLD Session
# Table structure one (one varchar(10), two smallint)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

engine = create_engine('sqlite:///orm.db')
connection = engine.connect()

class One(Base):
    __tablename__ = 'one'

    one = Column(String(10),
                nullable=False,
                default='papi'
                )
    two = Column(Integer,
                
                )