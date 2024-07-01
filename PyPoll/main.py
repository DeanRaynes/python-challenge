#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import csv

rowcount = 0
votes = {}

csvpath = os.path.join('.','Resources','election_data.csv')

output_file = os.path.join('.','Analysis','Election_Results.txt')

with open(csvpath, encoding='utf') as election_csv:
    csvreader = csv.reader(election_csv, delimiter=',')

    header = next(election_csv)


    for row in csvreader:
        rowcount+= 1 
        candidate = row[2]
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

winner = max(votes, key=votes.get)


output = (
    f"Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {rowcount}\n"
    f"-----------------------\n"
)
for candidate, vote_count in votes.items():
    percentage = vote_count / rowcount * 100
    output += f"{candidate}: {percentage:.3f}% ({vote_count})\n"

output += (
    f"-----------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------\n"
)

print(output)

with open(output_file, 'w') as file:
    file.write(output)


# In[ ]:




