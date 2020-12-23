import os 
import csv
months = 0
net_total = 0
greatest_increase = 0
#average_change = 0
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # test that code is accessing csv file
    print(csvreader)
    for row in csvreader:
        months += 1
        net_total += int(row[1])
        next_row = next(csvreader)
              
    
        
    
   # average_change = net_total / months ----this is not correct
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(net_total))
   # print(greatest_increase_month)
    print(greatest_increase)
   # print("Average Change: " + str(average_change))
    