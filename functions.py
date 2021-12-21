#Import the method for calculating degree of profanity from the dictionary file created previously
from dictionary import calculate_profanity

#Import required functions from SQLAlchemy library
from sqlalchemy import select, insert, exists

#This method checks the profanity of a tweet by the tweet ID
def profanity_by_id(tweet_id, conn, user, tweets, profanity_index):

  #Check if the tweet_id passed to the function exists in the profanity_index table
  if conn.execute(select(profanity_index.c.tweet_id).where(profanity_index.c.tweet_id == tweet_id)).fetchone():

    #Select the tweet_id, the tweet, and the profanity and return it
    s = select(profanity_index.c.tweet_id,tweets.c.tweet,profanity_index.c.profanity).where(profanity_index.c.tweet_id == tweet_id and tweets.c.tweet_id == tweet_id)
    result = conn.execute(s).fetchone()
    return result
  
  #Check if the tweet_id passed to the function exists in the tweets table
  elif conn.execute(select(tweets.c.tweet_id).where(tweets.c.tweet_id == tweet_id)).fetchone():

    #Select the tweet_id and tweet
    s = select(tweets.c.tweet_id,tweets.c.tweet).where(tweets.c.tweet_id == tweet_id)
    result = conn.execute(s).fetchone()
    id = result[0]

    #Split the tweet into a list of words and calculate its profanity
    tweet = result[1].split()
    deg = calculate_profanity(tweet)

    #Insert the calculated profanity into the profanity_index table
    ins = profanity_index.insert()
    conn.execute(ins,{"tweet_id":id,"profanity":deg})

    #Return the tweet_id, tweet, and profanity
    return (id,result[1],deg)
  
  else:
    return "Tweet ID does not exist"

#This method checks the profanity of tweets from a list of tweet IDs
def process_list(id_list, conn, user, tweets, profanity_index):

  for id in id_list:
    
    #call the ID-wise profanity check
    print(profanity_by_id(id,conn, user, tweets, profanity_index))

#This method checks the profanity of all the tweets in the database
def process_all(conn, user, tweets, profanity_index):

  #Select the tweet IDs of all the tweets
  s = select(tweets.c.tweet_id)
  result = conn.execute(s)

  #Call the method to check profanity from a list of tweet IDs
  process_list([row[0] for row in result], conn, user, tweets, profanity_index)