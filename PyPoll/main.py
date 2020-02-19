import os
import csv

election_file = os.path.join("/Users/leah/python-challenge/PyPoll/Resources/election_data.csv")
with open(election_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)

#create empty lists to hold information from csv
    votes=[]
    candidates=[]

    for row in csvreader:
        votes.append(row[0])
    

#need a dictionary for the candidates

#final results
    print("Election Results")
    print("--------------------------------")
    print(f'Total votes: {len(votes)}')
    print("--------------------------------")
    