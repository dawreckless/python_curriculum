# What you will learn
#   - Logical Operators
#   - Review of Comparison Operators
#   - Review of if, else, elif statements
#   - Review of Assignment Operators

# Logical Operators -> used for conditional statements
# and - True if ALL conditions are True
# or  - True if ANY condition is True
# not - Reverses True/False

height = float(input("Enter height (in feet): "))
age = int(input("Enter your age: "))

# Review
if height == 5.75:
    print("You are the height of the average man!")
elif height == 5.3:
    print("You are the height of the average woman!")

# Using AND (both must be true)
if height > 6 and age > 18:
    print("You are a tall adult!")

# Using OR (only one must be true)
if age < 5 or height < 3:
    print("You are very small or very young!")

# Using NOT (opposite)
if not(age >= 13):
    print("You are not a teenager yet!")
