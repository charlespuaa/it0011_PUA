# Activity 5
# Pua, Charles Michael G.
# TW23

def divide():
    try:
        num1 = int(input("Enter first number: "))           
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            return None
        else:
            return num1/num2
    except ValueError:
        return None
    
def exponent():
    try:
        num1 = int(input("Enter base number: "))           
        num2 = int(input("Enter exponent number: "))
        return num1**num2
    except ValueError:
        return None
    
def remainder():
    try:
        num1 = int(input("Enter first number: "))           
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            return None
        else:
            return num1%num2
    except ValueError:
        return None
    
def summation():
    try:
        num1 = int(input("Enter first number: "))           
        num2 = int(input("Enter second number: "))
        if num2 < num1:
            return None
        else:
            return sum(range(num1, num2+1))
    except ValueError:
        return None

def main():
    while True:
        print("Choose an operation:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        choice = input("Enter choice: ").upper()
        
        if choice == 'D':
            result = divide()
            if result is not None:
                print("Result:", result)
            else:
                print("Invalid input")
        elif choice == 'E':
            result = exponent()
            if result is not None:
                print("Result:", result)
            else:
                print("Invalid input")
        elif choice == 'R':
            result = remainder()
            if result is not None:
                print("Result:", result)
            else:
                print("Invalid input")
        elif choice == 'F':
            result = summation()
            if result is not None:
                print("Result:", result)
            else:
                print("Invalid input")
        elif choice == 'Q':
            break
        else:
            print("Invalid choice")
            
main()

