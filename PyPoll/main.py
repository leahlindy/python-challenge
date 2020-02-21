import os
import csv

election_file = os.path.join("/Users/leah/python-challenge/PyPoll/Resources/election_data.csv")
with open(election_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)
    
    #empty dictionary to hold information from csvfile
    votedictionary = {}
    num_votes = 1


    #loop through rows to add voting information to dictionary
    # Key: Row[2]- candidate name
    # Value: list of candidate votes and percent votes received
    # Continue adding votes at the end of the loop (before going to next row)
    
    for row in csvreader:
        
        #iterate through unique names and add to dictionary
        #set up candidate vote count- add one each time candidate is found in reader
        if row[2] in votedictionary:
            candidate_vote= votedictionary.get(row[2],0)[0]+1
            #dictionary key: candidate name, value (list): [vote count, percent]
            votedictionary[row[2]] = [candidate_vote, (candidate_vote/num_votes)*100]
        
        else:
            #if not in dictionary it is the first vote for the candidate (num_votes=1)
            votedictionary[row[2]]=[num_votes,1/num_votes]
        
        #before exiting the iteration need to add one to total vote count
        num_votes += 1

    
    #determine a winner
    #leader starts at 0, will be changed each time candidate vote is greater than last leader value (each iteration leader is subject to change)
    leader = 0
    # iterate through the candidates in dictionary 
    for key, value in votedictionary.items():
        # if vote count of candidate is largest so far it is stored as current leader 
        if value[0] > leader:
            leader = value[0]
            # store candidate name (if it is current leader)
            winner = key
        else:
            pass


#final results- round percentages in f'string
    print('`')
    print("Election Results")
    print("--------------------------------")
    print(f'Total votes: {(num_votes)}')
    print("--------------------------------")
    print(f'Khan: %{round((votedictionary["Khan"][1]),3)} ({votedictionary["Khan"][0]})')
    print(f'Correy: %{round((votedictionary["Correy"][1]),3)} ({votedictionary["Correy"][0]})')
    print(f'Li: %{round((votedictionary["Li"][1]),3)} ({votedictionary["Li"][0]})')
    print("O'Tooley: %" + str(round((votedictionary["O'Tooley"][1]),3)) + " (" + str(votedictionary["O'Tooley"][0])+ ")" )
    print("--------------------------------")
    print(f'Winner: {winner}')
    print("--------------------------------")