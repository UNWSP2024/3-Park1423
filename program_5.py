##
# Code by Parker Jolly
# 9/18/2025
# Name: Hot dog ordering program
##

TAX = 0.07

#Figure out what kind of hotdog we want and properly set our starting total.

hotdogType = input("Would you like a Hot Dog ($3.50), or a Chili Dog ($4.50)? ").lower().replace(" ","")
if hotdogType == "chilidog":
    total = 4.50
elif hotdogType == "hotdog":
    total= 3.50
else:
    print("That wasn't an option!")

#Ask which toppings we want add the necassary amount to our total.
toppingInput = input("Would you like cheese ($0.50) on that? Y/N  ").lower().replace(" ","")
if toppingInput == "y":
    total += 0.50

toppingInput = input("Would you like peppers ($0.75) on that? Y/N  ").lower().replace(" ","")
if toppingInput == "y":
    total += 0.75

toppingInput = input("Would you like grilled onions ($1.00) on that? Y/N  ").lower().replace(" ","")
if toppingInput == "y":
    total += 1.00

#Go down a line then print the subtotal, tax, and total.
print("")
print(f"Subtotal: {total:.2f}")
print(f"Tax: {total * TAX:.2f}")
print(f"Total: {total * (TAX + 1):.2f}")

