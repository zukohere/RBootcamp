# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for line in csvreader:
        if line[0] == video:
            print(line[0] + "is rated " + line[1] + " with a score of " +line[5])
            break
        
        
