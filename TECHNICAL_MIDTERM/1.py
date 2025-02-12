def check_palindrome(num):
    return str(num) == str(num)[::-1]

file1=open("numbers.txt", "r")
lines = file1.readlines()
file1.close()

for line_number, line in enumerate(lines, 1):
      numbers = [num.strip() for num in line.split(',') if num.strip().isdigit()]
      numbers = [int(num) for num in numbers]
      
      if numbers:
            total = sum(numbers)
            result = "This sum is a palindrome." if check_palindrome(total) else "This sum is not a palindrome."
            formatted_numbers = ', '.join(str(num) for num in numbers)
            print(f"Line {line_number}: {formatted_numbers} (Sum: {total}) - {result}")