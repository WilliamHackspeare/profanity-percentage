# profanity-percentage

Given a file of tweets and a set of racial slurs, the task is to find the percentage of profanity present in each tweet.

Basic Assumptions:
- The tweets are saved in an SQL database
- The list of words is provided to us in a dictionary as a JSON file
- The degree of profanity is given by: <img src="https://render.githubusercontent.com/render/math?math=\frac{\text{Number of profane words}}{\text{Total number of words}}\times 100#gh-light-mode-only"><img src="https://render.githubusercontent.com/render/math?math=\color{white}{\frac{\text{Number of profane words}}{\text{Total number of words}}\times 100}#gh-dark-mode-only">
- The degree of profanity for each tweet is calculated by the program and stored in the SQL database
