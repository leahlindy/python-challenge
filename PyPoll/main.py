import os
import csv
from collections import Counter

election_file = os.path.join("/Users/leah/python-challenge/PyPoll/Resources/election_data.csv")
with open(election_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)

#create empty lists to hold information from csv
    
    #number of votes for candidates
    votedictionary={}

            
    num_votes = 1
    for row in csvreader:
        if row[2] in votedictionary:
            candidate_vote= votedictionary.get(row[2],0)[0]+1
            votedictionary[row[2]] = [candidate_vote, (candidate_vote/num_votes)*100]
        else:
            votedictionary[row[2]]=[num_votes,1/num_votes]
        num_votes += 1

    print(num_votes)     

    print(votedictionary)



#final results
    print("Election Results")
    print("--------------------------------")
    #print(f'Total votes: {(num_votes)}')
    print("--------------------------------")
    print(f'Khan: % ({votedictionary["Khan"][1]})')
    print(f'Correy: % ({votedictionary["Correy"]})')
    print(f'Li: % ({votedictionary["Li"]})')
    #print(f'O\'Tooley: % ({votedictionary["O'\Tooley"]})')
    #print(num_votes[0])
    #print(round(num_votes[0]/len(votes)*100),3)
    #print(f'Winner: {winner}')
   
    
    