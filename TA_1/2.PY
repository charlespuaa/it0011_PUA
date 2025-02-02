s = input("Enter a string with numbers: ")
print("Sum of digits:", sum(int(c) for c in s if c.isdigit()))
