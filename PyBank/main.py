import os
import csv

csvpath = os.path.join('.','Resources','budget_data.csv')

with open(csvpath, encoding='utf') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")

    rowcount = sum(1 for row in csvreader)


print("Financial Analysis")
print("--------------------------------")

print("Total Months:", rowcount)
