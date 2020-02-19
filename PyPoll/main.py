import os
import csv
from collections import Counter

election_file = os.path.join("/Users/leah/python-challenge/PyPoll/Resources/election_data.csv")
with open(election_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)

#create empty lists to hold information from csv
    votes=[]
    candidates=[]
    #number of votes for candidates
    num_votes=[]
    votedictionary={}

# iterate over rows in file
    for row in csvreader:
        votes.append(row[0])
        #if not in existing list, add to list of unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            num_votes.append(1)
        else:
        #if candidate already exists, add a vote for that candidate
            candidate_index = candidates.index(row[2])
            num_votes[candidate_index] += 1
    print(candidates)
    print(num_votes)
#create a dictionary to hold candidate votes
    for candidate in candidates:
        votedictionary[candidate]=[0,0]
        for key, value in votedictionary.items():
            if candidate == row[2]:
                value[1]= value[1]+1
                break
            else:
                pass


    print (votedictionary["Khan"])
    for row in csvreader:
        #items() method is used to return the list with all dictionary keys with values. 
        #Returns: A view object that displays a list of a given dictionary's (key, value) tuple pair
        #iterate through the empty dictionary to add idems
        for key,value in votedictionary.items():
            print (f'tuple {votedictionary}')
    

    

#need a dictionary for the candidates

#final results
    print("Election Results")
    print("--------------------------------")
    print(f'Total votes: {len(votes)}')
    print("--------------------------------")
    
    