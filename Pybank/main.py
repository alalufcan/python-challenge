# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# (check)The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

import os
import csv
import datetime
pybank_csv = os.path.join('pybank.csv')

num=[]
total=0
average_change = []
greatest_increase = []
greatest_decrease = []
with open(pybank_csv, newline='') as csvfile:

    pybank_csv = csv.reader(csvfile, delimiter=',')


    def number_of_months(pybank_csv):
        dates = str(pybank_csv[0])
        pl = int(pybank_csv[1])
    for i in pybank_csv:
        num.append(i)
        
    print(len(num)-1)

# profitandloss=0
#     for i in pybank_csv[1]:
#         profitandloss=profitandloss+i

#     print(profitandloss)

    for column in pybank_csv:
        pl= pybank_csv[1]
            for row in pl:
                





