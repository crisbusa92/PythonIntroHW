import os
import csv
# Set path for data file
csvpath = os.path.join('Resources','pybank.csv')

with open(csvpath,'r') as datafile:
    #Set Comma as delimiter
    datafile = csv.reader(datafile, delimiter=',')
    #Set Variables to start
    monthnum = 0
    pl = 0
    pnls = []
    #Skip header row
    next(datafile, None)
    #Loop opps to get results
    for row in datafile:
        #Find number of total months
        monthnum = monthnum + 1
        #Find total P&L for all periods
        pl= pl + int(row[1])
        #Greate new list to average
        pnls.append(row)

    
#print results to check    
print (monthnum)
print (pl)



