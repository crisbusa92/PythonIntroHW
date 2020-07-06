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
    khanv = 0
    correyv = 0
    liv = 0
    otooleyv = 0
    

    for row in datafile:
        #Total voters
        voters = voters + 1
        #List of candidates
        if row[2] not in candidate:
            candidate.append(row[2])
        #Votes per Cadidate
        if row[2] == candidate [0]:
            khanv = khanv + 1
        elif row[2] == candidate [1]:
            correyv = correyv + 1
        elif row[2] == candidate [2]:
            liv = liv + 1
        elif row[2] == candidate [3]:
            otooleyv = otooleyv + 1
khanp = "{:.2%}".format(khanv/voters)
correyp = "{:.2%}".format(correyv/voters)
lip = "{:.2%}".format(liv/voters)
otooleyp = "{:.2%}".format(otooleyv/voters)
#New lists for Votes and Percentages
khan = [khanv,khanp]
correy = [correyv, correyp]
li = [liv,lip]
otooley = [otooleyv,otooleyp]
#New Dictionary for Cadidate : [Votes,percentage of total]
canvot = {candidate[0]:khan,candidate[1]:correy,candidate[2]:li,candidate[3]:otooley}
#determine winner
winner = max(canvot, key=canvot.get)
#Print results for testing
#print(voters)
#print(len(candidate))
#print(canvot)
#print(winner)
#print(canvot)

#Print Results to txt
print(
    f'Election Results \n'
    f'---------------- \n'
    f'Total Votes {voters} \n'
    f'---------------- \n'
    f'Khan: {khanp} ({khanv})\n'
    f'Correy: {correyp} ({correyv}) \n'
    f'Li: {lip} ({liv}) \n'
    f"O'Tooley {otooleyp} ({otooleyv}) \n"
    f'---------------- \n'
    f'Winner: {winner} \n'
    f'---------------- \n'
)

poll = (
    'Election Results \n'
    '---------------- \n'
    'Total Votes ' +str(voters)+'\n'
    '----------------' '\n'
    'Khan: '+str(khanp)+' ('+str(khanv)+')\n'
    'Correy: '+str(correyp)+' ('+str(correyv)+')\n'
    'Li: {'+str(lip)+' ('+str(liv)+')\n'
    "O'Tooley "+str(otooleyp)+' ('+str(otooleyv)+')\n'
    '----------------' '\n'
    'Winner: '+str(winner) +'\n'
    '----------------' '\n'
)

#Export file
#Set Path for Output and name .txt flile
txtpath = os.path.join('Analysis','Poll.txt')

#Write txt file
txtfile= open(txtpath, 'w')
txtfile.write(poll)
