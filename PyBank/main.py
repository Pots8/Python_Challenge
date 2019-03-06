import os
import csv

file_input = "Resources/budget_data.csv"
file_output = "financial.txt"

# Initialize parameters
total_months = 0
income_change_list = []
maximum_INT = 2**63 - 1
ZERO = 0
maximum_increase = [None, ZERO]
maximum_decrease = [None, maximum_INT]
total_income = 0

# open file to read
with open(file_input) as profitloss_data:
    reader = csv.DictReader(profitloss_data)
    # initialize and store data
    one_header = next(reader)
    total_months += 1
    total_income = int(one_header["income"])
    last_income = int(one_header["income"])

    for row in reader:
        total_months += 1
        total_income += int(row["income"])
        #  Count diff
        income_change = int(row["income"]) - last_income
        last_income = int(row["income"])
        income_change_list +=  [income_change]
        # Find maximum increase
        if income_change > maximum_increase[1]:
            maximum_increase = [row["Date"], income_change]

        # Find maximum decrease
        if income_change < maximum_decrease[1]:
            maximum_decrease = [row["Date"], income_change]

# Find average
avg_income = sum(income_change_list) / len(income_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_income}\n"
    f"Average income Change: ${avg_income}\n"
    f"maximum Increase in Profits: {maximum_increase[0]} (${maximum_increase[1]})\n"
    f"maximum Decrease in Profits: {maximum_decrease[0]} (${maximum_decrease[1]})\n")

print(output)

# output to text file
with open(file_output, "w") as txt_file:
    txt_file.write(output)
