# Tip Calculator

percentage = 100
print("Welcome to the tip calculator.")
bill = input("What is your total bill? $")
tip = input("What percentage tip would you like to give 10, 12 or 15?")
split = input("How many people to split the bill? ")

tip_cal = float(bill) / int(percentage) * int (tip)
split_cal = float(tip_cal) / int(split)
bill_cal = float(bill) / int(split)
total_bill = float(bill_cal) + float(split_cal)
final_amount = "{:.2f}".format(total_bill, 2) # round(totall_bill,2)
print(f"Each person should pay ${final_amount}")