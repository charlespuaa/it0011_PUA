# 3.3 String Manip, File Handling 
# Pua, Charles

fName = input("Enter first name: ")
lName = input("Enter last name: ")
age = input("Enter age: ")
contactNumber = str(input("Enter contact number: "))
course = input("Enter course: ")
fullName = fName + " " + lName
info = f"Full Name: {fullName}\nAge: {age}\nContact Number: {contactNumber}\nCourse: {course}"

f = open("students.txt", "w")
write = info
f.writelines(write)
f.close

print("Student informaton has been saved to students.txt")
