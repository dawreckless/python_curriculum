

color = input("Enter a color: ")
# String
if color == "red":
    print("You chose red (string comparison).")
print()  # blank line 

age = int(input("Enter your age: "))
# Integer
if age >= 18:
    print("You are an adult (integer comparison).")
print()  # blank line 

height = float(input("Enter your height in feet: "))
# Float
if height < 5.5:
    print("You are below average height (float comparison).")
print()  # blank line 

is_student = input("Are you a student? (yes/no): ")
# Boolean
student_bool = bool(input("Are you a student? (True or False): ")

if student_bool == True:   
    print("You are a student (boolean comparison).")
print()  # blank line 
