height = float(input("Enter your height in feet: "))
age = int(input("Enter your age: "))

if height >= 4 and age >= 10:
    print("You can ride!")
elif height >= 4 or age >= 10:
    print("You can ride with adult supervision.")
elif not (height >= 4):
    print("You cannot ride.")
else:
    print("Invalid input.")
