
stringg = input("Enter a string: ")
vowels = "aeiouAEIOU"
v, c, sp, o = 0, 0, 0, 0

for char in stringg:
    if char in vowels:
        v += 1
    elif char.isalpha():
        c += 1
    elif char.isspace():
        sp += 1
    else:
        o += 1

print(f"Vowels: {v}, Consonants: {c}, Spaces: {sp}, Others: {o}")
