class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}"


class StudentManager:
    def __init__(self):
        self.students = {}

    def addStudent(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id in self.students:
                raise ValueError("Student ID already exists.")
            
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            
            course = input("Enter Student Course: ")
            
            self.students[student_id] = Student(student_id, name, age, course)
            print("Student added successfully.")
        except ValueError as e:
            print("Error:", e)

    def viewStudents(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                print(student)

    def updateStudent(self):
        try:
            student_id = input("Enter Student ID to update: ")
            if student_id not in self.students:
                raise ValueError("Student ID not found.")

            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            
            course = input("Enter new course: ")
            
            self.students[student_id] = Student(student_id, name, age, course)
            print("Student updated successfully.")
        except ValueError as e:
            print("Error:", e)

    def deleteStudent(self):
        try:
            student_id = input("Enter Student ID to delete: ")
            if student_id not in self.students:
                raise ValueError("Student ID not found.")
            
            del self.students[student_id]
            print("Student deleted successfully.")
        except ValueError as e:
            print("Error:", e)


def main():
    manager = StudentManager()
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.addStudent()
        elif choice == "2":
            manager.viewStudents()
        elif choice == "3":
            manager.updateStudent()
        elif choice == "4":
            manager.deleteStudent()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
