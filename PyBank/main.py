import os 
import csv
months = 0
net_total = 0
greatest_increase = []
greatest_decrease = []
net_change_list =[]
average_change = 0
total_difference = 0
difference = 0
month_of_change = []
monthly_difference = {}
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    prev_net_change = int(first_row[1])
    months += 1
    net_total += int(first_row[1])


    for row in csvreader:
        months += 1
        net_total += int(row[1])
        
        
        net_change = int(row[1]) - prev_net_change
        prev_net_change = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = row[1]


    
       # difference = int(next_row[1]) - int(row[1])
        #print(difference)
         #monthly_change = {row: difference}
    #print(monthly_difference)

# monthly_difference["key1"] = [month_of_change]
# monthly_difference["key2"] = [net_change_list]

# print(monthly_difference)


average_change = round(sum(net_change_list) / len(net_change_list), 2)
# monthly_difference = {month_of_change: net_change_list}
#greatest_increase = max(monthly_difference, key=monthly_difference.get)

print(greatest_increase)

    
# Create a list of the change between months. Fill this into a dictionary to get the month. 
# Use append function to create the new list. Need to do math on the values ahead somehow
    


print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average_change))
# # print(greatest_increase_month)
# print(greatest_increase)
# # print("Average Change: " + str(average_change))