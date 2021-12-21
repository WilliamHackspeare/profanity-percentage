# profanity-percentage

## Problem Statement
Given a file of tweets and a set of racial slurs, the task is to find the percentage of profanity present in each tweet.

## Basic Assumptions  
- The tweets are saved in an SQL database
- The list of words is provided to us in a dictionary as a JSON file
- The degree of profanity is given by: <img src="https://render.githubusercontent.com/render/math?math=\frac{\text{Number of profane words}}{\text{Total number of words}}\times 100#gh-light-mode-only"><img src="https://render.githubusercontent.com/render/math?math=\color{white}{\frac{\text{Number of profane words}}{\text{Total number of words}}\times 100}#gh-dark-mode-only">
- The degree of profanity for each tweet is calculated by the program and stored in the SQL database

## Database
The database structure upon which the program functions contains three tables, containing the basic details of the users, the tweets and the profanity indexes in another.  
The current database structure modeled in the program leaves much to be desired in relation to a practical database, such as user details, date and time information of the tweets, and further details about the profanity, but it works for a demonstration of principles.  
The SQL engine and file format being used here is SQLite, version 3.

The schema and entity relationship diagram (ERD) of the database is given below:  

<img src="/assets/Schema.png">  

<img src="/assets/ERD.png">

## List of Banned Words
The set of racial slurs (also referred to in the documentation as 'bad' or 'banned' words or profanity) is assumed to be stored as a JSON file, containing a JSON Object, which can be easily converted into a Python dictionary. The keys will be a positional index, while the values are the words themselves.  

The file contents will be in the format shown below:  

```json
{
  "1":"Word1",
  "2":"Word2"
}
```

## Program Structure and Logic
The code for the program is divided into four segments:  
- database.py
- dictionary.py
- functions.py
- main.py  

### database.py
This file contains the methods which initialises the database for the program.  
The SQLAlchemy toolkit is used in this program for the purpose of database handling. The engine is initialised and the tables and their mappings are created and connected to the datbase.

### dictionary.py
This file contains the methods to load the JSON file into a dictionary and check if the string passed to the function is a bad word or not, and calculate the degree of profanity of a list of words passed to the method.

### functions.py
This file contains the primary processing methods of the program.  
It contains functions that cross check a tweet by id from the database and give their degree of profanity, give the degrees of profanity for a list of tweet ids, and do the same for all the tweets in the database.  
A crucial choice that was made here was the use of a modular approach in place of a monolithic approach for the calculation. This would increase the time it took to process the table, but provide greater flexibility.

### main.py
This file is the primary executable file. It extracts the database objects from database.py and passes them to the function from functions.py.

There are several potential and required improvments that would need to be made before this program can be used on databases of scale, such as batch processing for faster processing.
