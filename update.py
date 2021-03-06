#!/usr/bin/python3
# PLD Session
# Table structure one (one varchar(10), two smallint)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData

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
        return self.one + " " + str(self.two)

# Create a new table
metadata = MetaData()
two = Table('two', metadata,
    Column('id', Integer, primary_key=True),
    Column('content', String(16), nullable=False)
)
class Two(object):
    def __init__(self, content):
        self.content = content

two.create(engine, checkfirst=True)

# Link Models to get data
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Print content from table ONE
for one in session.query(One).all():
    # Using def __str__ can use -> print(one)
    print("Field One:{} - Field Two:{}".format(one.one, one.two))

# Insert content to table TWO
# insertQuery = Two.insert().values(content="Vamos Tio de vuelta")

# Update content on table TWO
mapper(Two, two)
session.query(Two).filter_by(id=3).update({'content': 'This is the new value Tio'})

# Print SQL Alchemy Query
#print(updateQuery)

#connection.execute(insertQuery)
for two in session.query(Two).all():
    print("id:{} - content:{}".format(two.id, two.content))

session.close()
connection.close()
