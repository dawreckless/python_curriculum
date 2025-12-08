# What you will learn
#   - if, else, elif statement
#   - Comparison Operators
#   - Assigment Operators

# if - else statement
# IF a condition is True do something
# Else do something else


# Comparison Operators - Very important!

# == -> is equal to
# > -> is greater than
# < -> is less than
# >= -> is greater than or equal to
# <= -> is less than or equal to
# != -> not equal to

# == vs. =
# ==  is a comparison operator, meaning it asks if something equals something else
# = is an assignment operator, meaning it sets something equal to something else

#Variables
age = int(input("Enter age: "))

if age >= 65: 
    print("You are a senior")
elif age >= 18: # Else if statements run if the if statement is false
    print("You are an adult!")
elif age < 0:
    print("How are you typing this? You are not born yet!")
else:
    print("You are not an adult!")

#Always put the MOST specific condition first
          
