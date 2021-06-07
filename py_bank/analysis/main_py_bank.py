import csv
import os

file_path = os.path.join("..","Resources", "budget_data.csv")
save_path = os.path.join("test_py_bank.txt")

all_months = []
all_profit = {}
total_months = 0
total_profit = 0
prev = 0
great_inc_name = ""
great_inc_value = 0
great_dec_name = ""
great_dec_value = 0
avg_total = 0

with open(file_path) as budget:
    reader = csv.reader(budget)
    header = next(reader)
    for row in reader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        if total_months > 1:
            temp =  int(row[1]) - prev
            avg_total = avg_total + temp
            if temp > great_inc_value: 
                great_inc_value = temp
                great_inc_name = row[0]
            elif temp < great_dec_value:
                great_dec_value = temp 
                great_dec_name = row[0]
        prev = int(row[1])
    avg_total = avg_total/(total_months - 1)

       
print ("Financial Analysis\n")
print("---------\n")
print(f"Total Months:{total_months}\n")
print(f"Total Profit:${total_profit}\n")
print(f"Average Change:${round(avg_total,2)} \n")
print(f"Greatest Increase in Profits: {great_inc_name} (${str(great_inc_value)})\n")
print(f"Greatest Decrease in Profits: {great_dec_name} (${str(great_dec_value)})\n")

with open (save_path, "w") as results:
    results.write ("Financial Analysis\n")
    results.write("---------\n")
    results.write(f"Total Months:{total_months}\n")
    results.write(f"Total Profit:${total_profit}\n")
    results.write(f"Average Change:${round(avg_total,2)} \n")
    results.write(f"Greatest Increase in Profits: {great_inc_name} (${str(great_inc_value)})\n")
    results.write(f"Greatest Decrease in Profits: {great_dec_name} (${str(great_dec_value)})\n")


