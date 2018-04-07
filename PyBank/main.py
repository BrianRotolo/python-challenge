#import os and write csv path
import pandas as pd
import numpy as np
import os
import csv

csvpathdf = "Resources/budget_data_1.csv"
budgetdf = pd.read_csv(csvpathdf)
#budgetdf.head()

csvpath = os.path.join("Resources", "budget_data_1.csv") 

#total months
months = budgetdf["Date"].count()
#months

#total revenue
revenue = budgetdf["Revenue"].sum()
#revenue

#average for period, don't need this for problem
#average = budgetdf["Revenue"].mean()
#average

#where things get weird
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

    
    
    
    
    #stuff I need to find
    dates = []
    revenues = []
    
    #loop needs to be here
    for numsearch in csvlist:
        dates.append(numsearch[0])
        revenues.append(int(numsearch[1]))
    
    #other stuff I need to find
    averagechange = []
    averagechange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    totalaveragechange = mean(averagechange)

    bigmonth = None
    largechange = max(averagechange)

    smallmonth = None
    smallchange = min(averagechange)
    
    
    
    
    #date loop big
    findbigmonth = None
    for row in csvlist:
        if findbigmonth is None:
            findbigmonth = int(row[1])
            continue
        if abs(int(row[1]) - findbigmonth) == largechange:
            bigmonth = row[0]
        findbigmonth = int(row[1])
    
    #date loop small (copied and pasted with small variables)
    findsmallmonth = None
    for row in csvlist:
        if findsmallmonth is None:
            findsmallmonth = int(row[1])
            continue
        if int(row[1]) - findsmallmonth == smallchange:
            smallmonth = row[0]
        findsmallmonth = int(row[1])


    
    with open("Output.txt", "w") as text_file:
    
        print("Financial Analysis", file=text_file)
        print("----------------------------", file=text_file)
        print(f"Total Months: {months}", file=text_file)
        print(f"Total Revenue: {revenue}", file=text_file)
        print(f"Average Revenue Change: {totalaveragechange}", file=text_file)
        print(f"Greatest increase in Revenue: {bigmonth} {largechange}", file=text_file)
        print(f"Greatest decrease in Revenue: {smallmonth} {smallchange}", file=text_file)
    