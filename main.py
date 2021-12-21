#Import the database initialization from the database file
from database import db_setup

#Import the method to process the entire table from the functions file
from functions import process_all

#Assign the database objects to variables
a,b,c,d = db_setup()

#Call the process function to calculate profanity
process_all(a,b,c,d)