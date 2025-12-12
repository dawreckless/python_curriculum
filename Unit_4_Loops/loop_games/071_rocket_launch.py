secret = 999

while True:
    guess = input("Enter passcode (or type 'cancel' to stop): ")

    if guess == "cancel":
        print("Launch canceled.")
        break

    if not guess.isdigit():  
        print("Invalid input.")
        continue

    guess = int(guess)

    if guess == secret:
        print("Correct!\n")
        break
    else:
        print("Wrong passcode.")

for i in range(5, 0, -1):
    print(i)

print("LAUNCH!")
