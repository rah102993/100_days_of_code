print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage of the bill would you like to give out? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
