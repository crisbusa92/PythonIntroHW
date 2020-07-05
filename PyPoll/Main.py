import os
import csv

#Set path for data file

csvpath = os.path.join('Resources','PyPoll.csv')

#Open and analyze file
with open(csvpath,'r') as datafile:
    datafile = csv.reader(datafile, delimiter=',')
    #Skip First Row
    next(datafile, None)
    #Define Variables
    voters = 0
    candidate = []
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    canvot = {candidate[0]:khan,candidate[1]:correy,candidate[2]:li,candidate[3]:otooley}


    for row in datafile:
        #Total voters
        voters = voters + 1
        #List of candidates
        if row[2] not in candidate:
            candidate.append(row[2])
        #Votes per Cadidate
        if row[2] == candidate [0]:
            khan = khan + 1
        elif row[2] == candidate [1]:
            correy = correy + 1
        elif row[2] == candidate [2]:







print(voters)
print(candidate)



