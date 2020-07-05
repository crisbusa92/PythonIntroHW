import os
import csv
# Set path for data file
csvpath = os.path.join('Resources','pybank.csv')
#define formula for average P&L
def average(x):
    return sum(x)/len(x)

with open(csvpath,'r') as datafile:
    #Set Comma as delimiter
    datafile = csv.reader(datafile, delimiter=',')
    #Set Variables to start
    monthnum = 0
    pl = 0
    pnls = []
    month = []
    greati = 0
    greatd = 0
    greatim = ''
    greatdm = ''

    #Skip header row
    next(datafile, None)

    #Loop opps to get results
    for row in datafile:

        #Find number of total months
        monthnum = monthnum + 1

        #Find total P&L for all periods
        pl= pl + int(row[1])

        #Greate new list to average
        pnls.append(int(row[1]))

        #Generate month list
        month.append(row[0])


#Find Greatest Increase and Greatest Decrease in profits
greati = max(pnls)
greatd = min(pnls)
#Find month for GreatestIncrease and GreatestDecrease        
greatim = month[pnls.index(greati)]
greatdm = month[pnls.index(greatd)]
#Print Results
print(
    f'Financial Analysis\n'
    '----------------------\n'  
    'Total Months {monthnum}\n' 
    'Total: ${pl}\n'
    'Greatest increase in profits: {greatim} ({greati}) \n'
    'Greatest decrease in profits: {greatdm} ({greatd})'
    )
