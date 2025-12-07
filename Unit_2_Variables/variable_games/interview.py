#User Input
#To get user input, type input() and set it to a variable
#The input is defaulted to a string
#If you do not want it to be a string, change the data type with datatype()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_male = bool(input("Are you male?: "))
gpa = float(input("What is your gpa?: "))
            
print("Hello " + name + ", your age is " + str(age) + ". It is " + str(is_male) + " that you are male, and your gpa is " + str(gpa) + ".")

