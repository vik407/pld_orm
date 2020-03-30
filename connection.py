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

# - - - - - - - - - 
# Create Model One
# - - - - - - - - - 
class One(Base):
    __tablename__ = 'one'

    one = Column(String(10),
                nullable=False,
                default='papi',
                primary_key=True
                )
    two = Column(Integer,
                nullable=False
                )
    def __str__(self):
        return self.one +" " +str(self.two)

# Link Models to get data
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for one in session.query(One).all():
        print(one)

session.close()