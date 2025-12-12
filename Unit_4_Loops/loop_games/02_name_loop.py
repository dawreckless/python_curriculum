# What you will learn:
#    - Review of while loop

name = "":

while name == "": #Remember: condition after while is ALWAYS True or False
  name = input("Enter name: ")
print("Hi, " + name)

#The loop repeats UNTIL the user inputs a name
#If they DO NOT input their name, they are prompted to input their name again
#When they input the name, the while loop is false.
#When the while loop is false, it goes to the next line.
