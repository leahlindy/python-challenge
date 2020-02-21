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
        if row[2] in votedictionary:
            candidate_vote= votedictionary.get(row[2],0)[0]+1
            votedictionary[row[2]] = [candidate_vote, (candidate_vote/num_votes)*100]
        else:
            votedictionary[row[2]]=[num_votes,1/num_votes]
        num_votes += 1

    
    #determine a winner
    #for value in votedictionary.values():
        #print(value[0]) 
    winner= votedictionary[row[2]][0]
    print(votedictionary)
    print(winner)

#final results- round percentages in f'string
    print("Election Results")
    print("--------------------------------")
    print(f'Total votes: {(num_votes)}')
    print("--------------------------------")
    print(f'Khan: % {round((votedictionary["Khan"][1]),5)} ({votedictionary["Khan"][0]})')
    print(f'Correy: % {round((votedictionary["Correy"][1]),4)} ({votedictionary["Correy"][0]})')
    print(f'Li: % {round((votedictionary["Li"][1]),4)} ({votedictionary["Li"][0]})')
    print("O'Tooley: % " + str(round((votedictionary["O'Tooley"][1]),4)) + " (" + str(votedictionary["O'Tooley"][0])+ ")" )
    print("--------------------------------")
    #print(f'The winner is{winner}!')
    print("--------------------------------")