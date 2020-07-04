import os
import csv
# Set path for data file
csvpath = os.path.join('Resources','pybank.csv')

with open(csvpath,'r') as datafile:
    #count number of rows/months starting at 0 and skipping the header
    monthnum = 0
    next(datafile, None)
    for row in datafile:
        monthnum = monthnum + 1
    
#print result to check    
print (monthnum)

