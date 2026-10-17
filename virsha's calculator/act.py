# Vrisha's Power Calculator Program

# 1. Ask the user for inputs
base = int(input("Enter the number: "))
exponent = int(input("Enter the power: "))

# 2. Set the initial result to 1
result = 1

# 3. Use a loop to multiply the number by itself 'exponent' times
for i in range(exponent):
    result = result * base

# 4. Display the final answer to her friends
print(f"Result: {base} raised to the power of {exponent} is {result}")
