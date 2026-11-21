print("welcome to the pizza deliveries")
size = input("what size pizza do you want? S, M, or L: ")
pepproni = input("do you want pepproni on pizza? y or n")
extra_chhese = input("do you want extra cheese? y or n")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepproni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_chhese == "y":
    bill += 1

print(f"your final bill is ${bill}")
