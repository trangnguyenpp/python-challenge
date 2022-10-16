import os
import csv

#store directory of the csv file
csvpath = os.path.join('..','Resources','election_data.csv')

#list to store data
ballot_id = []
candidates = []
unique_candidates = []
pct_results = []
results = ["Election Results","----------------------------"]

#open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    
    # read the header row 
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    for row in csvreader:
        #add ballot ID
        ballot_id.append(row[0]) 
        #add candidates
        candidates.append(row[2])

# calculate the number of votes
total_votes = len(ballot_id)
results.extend([f'Total Votes: {total_votes}',"----------------------------"])

# find unique candidates
unique_candidates = list(dict.fromkeys(candidates))

#calculate the pct of votes and total number of votes for each candidate
for candidate in unique_candidates:
    total = candidates.count(candidate)
    pct = round(total/total_votes,3)
    pct_results.append(pct)
    results.append(f'{candidate}: {pct}% ({total})')

#find the winner
winner_pct= max(pct_results)
results.extend(["----------------------------",
               f'Winner: {unique_candidates[pct_results.index(winner_pct)]}',
               "----------------------------"])

#set variable for output file
output_file = os.path.join('poll_analysis_results.txt')

#open the output file
with open(output_file, 'w') as datafile:
    for line in results:
        datafile.write(line)
        datafile.write('\n')
        print(line)