# Take input from the user
char = input("Enter a character: ")

# Ensure the input is exactly one character and falls within A-Z or a-z
if len(char) == 1 and (('a' <= char <= 'z') or ('A' <= char <= 'Z')):
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")
