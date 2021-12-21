#Import the json library to parse JSON file to Python
import json

#Import list of punctuation characters from the string library
from string import punctuation as p

#This method checks if the given word is a profanity
def is_profanity(word):

  #Open the JSON file
  words_file = open('data.json')

  #Parse the JSON file as a dictionary and extract the values
  bad_words = json.load(words_file).values()

  #Check and return if the word is a bad work
  return word in bad_words

#This method calculates the degree of profanity for a list of strings
def calculate_profanity(sentence):

  #Initialise the count of bad words
  count_bad = 0
  #Initialise the total count of words
  count = 0

  #Loop through the list of words
  for word in sentence:

    #Check if the word, stripped of any leading or trailing punctuations or spaces, is a bad word and update count
    if is_profanity(word.strip(p+" ")):
      count_bad += 1
    count += 1
  
  #Calculate the degree of the list
  deg = (count_bad/count)*100

  #Return the degree
  return deg