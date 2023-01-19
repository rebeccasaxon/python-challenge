#Import CSV
import os
import csv

#Create object
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Open and read the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Loop through rows 
    for row in csvreader:
        
        dates.append(row[0])
        
        # Calculate the change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Count total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Find greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Find greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Find average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Print Output
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Export putput to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))