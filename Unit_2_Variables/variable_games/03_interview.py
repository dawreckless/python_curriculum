#What you will learn
#   - Review of printing
#   - Review of concantenation
#   - User input
#   - Type casting

#User Input
#To get user input, type input() and set it to a variable
#The input is defaulted to a string
#If you do not want it to be a string, change the data type with the data type then () 

name = input("Enter your name: ") # default is string
age = int(input("Enter your age: ")) # int is integer
is_male = bool(input("Are you male?: ")) #bool is boolean
height = float(input("What is your height?: ")) 
            
print("My name is " + name)
print("My age is " + str(age))
print("The fact that I am male is " + str(is_male))
print("My height is " + str(height))

