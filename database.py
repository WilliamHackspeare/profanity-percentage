#Import required objects from the SQLAlchemy library
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey

#This method sets up the database
def db_setup():
  #Creates an engine (interface) to the given database
  db = create_engine("sqlite:///database.sqlite3")

  #Create a MetaData container object that binds features of the database being described
  md_obj = MetaData()

  #Define the table "user"
  user = Table('user',md_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name',String(30),nullable=False)
  )

  #Define the table "tweets"
  tweets = Table('tweets',md_obj,
    Column('tweet_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('tweet', String(280), nullable=False)
  )

  #Define the table "profanity_index"
  profanity_index = Table('profanity_index',md_obj,
    Column('tweet_id', Integer, ForeignKey("tweets.tweet_id"), primary_key=True),
    Column("profanity", Float)
  )

  #Connect the engine and create a connection object
  conn = db.connect()

  #Return the connection object and the table objects
  return conn,user,tweets,profanity_index