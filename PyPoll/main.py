import os
import csv

total_votes = 0
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

    
    

print("Election Results")
print("--------------------")
print("Total Votes: " + str(total_votes))
print("--------------------")