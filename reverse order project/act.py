# Take input from the user
num = int(input("Enter a number: "))

# Start the digit counter at 0
count = 0

# Special case: if the number is 0, it has 1 digit
if num == 0:
    count = 1

# Loop until the number shrinks to 0
while num > 0:
    count = count + 1   # Increase count by 1
    num = num // 10     # Remove the last digit

# Print the final result
print("Total digits:", count)
