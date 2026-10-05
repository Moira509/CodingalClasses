# Take input from the user
age = int(input("Enter the age: "))

# Outer conditional statement checking the lower bound
if age >= 10:
    # Inner (nested) conditional statement checking the upper bound
    if age <= 20:
        print("The age is between 10 and 20 years.")
    else:
        print("The age is not between 10 and 20 years.")
else:
    print("The age is not between 10 and 20 years.")
