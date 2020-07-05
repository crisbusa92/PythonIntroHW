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

    for row in datafile:
        #Total voters
        voters = voters + 1
        #List of candidates
        if row[2] not in candidate:
            candidate.append(row[2])
            




print(voters)
print(candidate)



