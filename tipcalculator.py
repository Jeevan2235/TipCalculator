print("Welcome to the tip calculator")

bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give?"))
people = int(input("How many people to split the bill?"))

amount_with_tip = tip / 100 * bill + bill
final_amount = (amount_with_tip / people)
final_amount_toal = round(final_amount, 2)

print(f"Each person should pay {final_amount_toal}")
