#!/usr/bin/env python
# coding: utf-8

# In[44]:


#Dependencies
import os
import csv

rowcount = 0
total = 0
previous_value = None
changes = []
max_increase = 0
max_increase_month = ""
max_decrease = 999999
max_decrease_month = ""

#loading file
csvpath = os.path.join('.','Resources','budget_data.csv')

output_file = os.path.join('.',"Budget_Analysis.txt")

with open(csvpath, encoding='utf') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")

    #setting header line
    header = next(budget_csv)

    # calculations
    for row in csvreader: 
        rowcount += 1
        total += int(row[1]) 
        current_value = int(row[1])
        

        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)

            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]

            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row [0]
                
        previous_value = current_value

average_change = sum(changes) / len(changes) if changes else 0

        


#analysis
output = (
    f"Financial Analysis\n"
    f"--------------------------------\n"
    f"Total Months: {rowcount}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n"
)

print(output)

with open(output_file, 'w') as file:
    file.write(output)


# In[ ]:




