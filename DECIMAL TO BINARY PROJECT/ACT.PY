print("Welcome to decimal to binary")

def decimal_to_binary(decimal_num):
    # Handle the special case where the input is 0
    if decimal_num == 0:
        return "0"
        
    binary_string = ""
    
    # Loop until the quotient becomes 0
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string = str(remainder) + binary_string  # Prepend the remainder
        decimal_num = decimal_num // 2                 # Integer division
        
    return binary_string

# Main program block to test the function
try:
    user_input = int(input("Enter a decimal number to convert: "))
    if user_input < 0:
        print("Please enter a non-negative integer.")
    else:
        result = decimal_to_binary(user_input)
        print(f"The binary representation of {user_input} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")



