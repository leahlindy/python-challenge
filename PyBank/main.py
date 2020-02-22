# open .csv
import os
import csv

budget_csv= os.path.join("./Resources/budget_data.csv")

#create empty lists to hold information from csv
month = []
revenue = []
revenue_change = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)
    
    #loop through rows, add information from each column (length and total can be determined)
    for row in csvreader:
        month.append(row[0])
        revenue.append(float(row[1]))
    
    #loop through revenue column only; generate list of each revenue change in range(column, row)
    for i in range (1,len(revenue)):
        revenue_change.append(revenue[i] - revenue[i-1])
        #calculate average change, length of revenue change list not revenue
        average_change = sum(revenue_change)/(len(revenue_change))

    #loop through revenue list wtih max/min function to find max change
        max_revenue_change = max(revenue_change)
        min_revenue_change = min(revenue_change)

    #Use index function to locate max/min change in revenue list
    #Use the revenue index to index into month list to return date of change 
        month_max = str(month[revenue_change.index(max_revenue_change)+1])
        month_min= str(month[revenue_change.index(min_revenue_change)+1])

        
    print ("Financial Analysis")
    print ("------------------------------")
    print (f'Total Months: {len(month)}')
    print (f'Total: ${sum(revenue)}')
    print(f'Average change: {round(average_change,2)}')
    print(f'Greatest Increase in Profits: {month_max} (${max_revenue_change})')
    print(f'Greatest Decrease in Profits: {month_min} (${min_revenue_change})')

with open('./output.txt', 'w') as f:
    print("Financial Analysis", file=f)
