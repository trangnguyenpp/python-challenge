import os
import csv

#store directory of the csv file
csvpath = os.path.join('..','Resources','budget_data.csv')

#list to store data
months = []
total = []
total_int = []
change = []
results = []

#open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    
    # read the header row 
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    for row in csvreader:
        #add months
        months.append(row[0]) 
        #add profits/losses
        total.append(row[1])
        total_int = [int(i) for i in total] #convert total list from string to integer
        
# calculate the number of months
total_months = len(months)

#calculate total profits/losses
total_earnings = sum(total_int)

#calculate average change
change = [b - a for a, b in zip(total_int, total_int[1:])]
average_change = round(sum(change)/len(change),2)
        
#find greatest increase in profits:
greatest_increase_in_profits = max(change)
greatest_decrease_in_profits = min(change)

# Print out the results:
results = ["Financial Analysis","----------------------------",
           f'Total months: {total_months}',
           f'Total: ${total_earnings}',
           f'average change: ${average_change}',
           f'Greatest Increase in Profits: {months[change.index(greatest_increase_in_profits)+1]} (${greatest_increase_in_profits})',
           f'Greatest Increase in Profits: {months[change.index(greatest_decrease_in_profits)+1]} (${greatest_decrease_in_profits})']

#set variable for output file
output_file = os.path.join('financial_analysis_result.txt')

#open the output file
with open(output_file, 'w') as datafile:
    for line in results:
        datafile.write(line)
        datafile.write('\n')
        print(line)