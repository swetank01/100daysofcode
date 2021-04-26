print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to slip:"))

total_bill += (total_bill / 100) * tip
bill_per_head = float(total_bill) / people
print(total_bill)
print(bill_per_head)

roundoff_bill = str(round(bill_per_head, 2))
#final_bill = "".format(bill_per_head)

print(f"Each Person should pay: $ {final_bill}")