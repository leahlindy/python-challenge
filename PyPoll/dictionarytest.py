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
    uniquevotes={}
    khan_count={}

# iterate over rows in file
    for row in csvreader:
        votes.append(row[0])
        #if not in existing list, add to list of unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        else:
            pass

#create a dictionary to hold candidate votes
    #this will just print out first value of value list created (store % and number votes in this list)
    #for candidate in candidates:
        #votedictionary[candidate]=[3,0]
    #print((votedictionary)["Li"][0])
    #for row in csvreader:
        #items() method is used to return the list with all dictionary keys with values. 
        #Returns: A view object that displays a list of a given dictionary's (key, value) tuple pair
        #iterate through the empty dictionary to add idems
        for candidate in candidates:
            uniquevotes[candidate]=[0,0]
        
    #for row in csvreader:
    for rows in csvreader: 
        for k,v in uniquevotes.items():
            if k == row[2]:
                uniquevotes["Khan"][0] + 1
                print (k)
    print(uniquevotes)

    #add values to dictionary- key will be over-written *need to += 1

        
   #for key, value in unique.items():
         #print(key)
    