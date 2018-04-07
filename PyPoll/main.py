import os
import csv
#didn't use, but in habit of starting code with
#import pandas as pd
#import numpy as np

#thank you for the link to the module index 
from collections import Counter

csvpath = os.path.join("Resources", "election_data_1.csv") 

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

   #set up for loop
    voterid = []
    county = []
    candidate = []
    
    #do the loop
    for numsearch in csvreader:
        voterid.append(numsearch[0])
        county.append(numsearch[1])
        candidate.append(numsearch[2])
    
    #stuff I need to find
    eachcandidate = set(candidate)    
    totalvote = len(voterid)
    
    #set up another loop
    candidname = []
    
    for row in eachcandidate:  
        candidname.append(row)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalvote}")
    print("-------------------------")
    
    #loop for results of each candidate (insert a ton of trial and error here)
    dictionary = {}
    candidvote = 0
    for row in candidname:
        #numbers
        actualcandid = str(candidname[candidvote])
        votes = candidate.count(actualcandid)
        votes = int(votes)
        percentage = round((votes / totalvote) * 100)
        #politician
        dictionary.update({actualcandid : votes})
        #print
        print(f"{actualcandid}: {percentage}% {votes}" )
        #next
        candidvote = candidvote + 1


    winner = max(dictionary, key=lambda key:dictionary[key])
    print("-------------------------")

    print("Winner: ", winner)