print("Welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))

tip = bill+(bill * tip / 100)
bill_per_person = tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")