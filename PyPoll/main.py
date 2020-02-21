import os
import csv

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

    
    #need to round values
    #determine a winner


#final results
    print("Election Results")
    print("--------------------------------")
    print(f'Total votes: {(num_votes)}')
    print("--------------------------------")
    print(f'Khan: % {round((votedictionary["Khan"][1]),5)} ({votedictionary["Khan"][0]})')
    print(f'Correy: % {round((votedictionary["Correy"][1]),4)} ({votedictionary["Correy"][0]})')
    print(f'Li: % {round((votedictionary["Li"][1]),4)} ({votedictionary["Li"][0]})')
    print("O'Tooley: % " + str(round((votedictionary["O'Tooley"][1]),4)) + " (" + str(votedictionary["Li"][0])+ ")" )
    #print(round(num_votes[0]/len(votes)*100),3)