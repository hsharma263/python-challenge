import os
import csv

total_votes = 0
khan_total_votes = 0
correy_total_votes = 0
li_total_votes = 0
otooley_total_votes = 0
candidates = {}

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan_total_votes += 1
        if row[2] == "Correy":
            correy_total_votes += 1
        if row[2] == "Li":
            li_total_votes += 1
        if row[2] == "O'Tooley":
            otooley_total_votes += 1


khan_percent = round(((khan_total_votes / total_votes) * 100), 3)
correy_percent = round(((correy_total_votes / total_votes) * 100), 3)
li_percent = round(((li_total_votes / total_votes) * 100), 3)
otooley_percent = round(((otooley_total_votes / total_votes) * 100), 3)


candidates = {"Khan": khan_total_votes, 
                "Correy": correy_total_votes,
                "Li": li_total_votes,
                "O'Tooley": otooley_total_votes
 }

winner = max(candidates, key=candidates.get)
    

print("Election Results")
print("--------------------")
print("Total Votes: " + str(total_votes))
print("--------------------")
print("Khan: " + str(khan_percent) + "%" + " ("+ str(khan_total_votes) + ")")
print("Correy: " + str(correy_percent) + "%" + " (" + str(correy_total_votes) + ")")
print("Li: " + str(li_percent) + "%" + " (" + str(li_total_votes)+ ")")
print("O'Tooley: " + str(otooley_percent) + "%" + " ("+ str(otooley_total_votes)+ ")")
print("--------------------")
print("Winner: " + winner)
print("--------------------")


# Need to export analysis to another csv 
