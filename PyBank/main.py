import os 
import csv
months = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
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
        

        if net_change > greatest_increase:
            greatest_increase_month = row[0]
            greatest_increase = net_change

        if net_change < greatest_decrease:
            greatest_decrease_month = row[0]
            greatest_decrease = net_change
    

average_change = round(sum(net_change_list) / len(net_change_list), 2)

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")



# Export analysis to text file 
output_path = os.path.join("analysis", "bank_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.writelines(["Financial Analysis \n",
    "--------------------------- \n",
    "Total Months: " + str(months) + "\n", 
    "Total: $" + str(net_total) + "\n",
    "Average Change: $" + str(average_change) + "\n",
    "Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ") \n",
    "Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ") \n",
     ])
txtfile.close()