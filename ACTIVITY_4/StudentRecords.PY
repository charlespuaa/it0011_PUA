# Student Record Management System
# Author: Charles Michael G. PUA
# Version: 1.0

import os

# Global variables
records = []
default_file = "Student_Records.txt"

def open_file(file_name=default_file):
    global records
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        records = []
        for line in lines:
            studentID, firstName, lastName, classStanding, majorExam = line.strip().split("|")
            records.append((studentID, (firstName, lastName), float(classStanding), float(majorExam)))
        print(f"\t\tFile '{file_name}' loaded successfully.")
    except FileNotFoundError:
        print(f"\t\tFile '{file_name}' not found. No records loaded.")

def save_records(file_name=default_file):
    with open(file_name, 'w') as file:
        for record in records:
            file.write(f"{record[0]}|{record[1][0]}|{record[1][1]}|{record[2]}|{record[3]}\n")
    print(f"Records saved successfully to '{file_name}'.")

def save_as_records():
    new_file_name = input("Enter new filename (with .txt extension): ")
    save_records(new_file_name)
    print(f"Records saved successfully as '{new_file_name}'.")

def display_all_records():
    while True:
        print("\nDisplay Options:")
        print("1. Order by Last Name")
        print("2. Order by Grade")
        print("3. Back to Main Menu")
        choice = input("Enter your choice (number): ")
        if choice == '1':
            display_by_last_name()
        elif choice == '2':
            display_by_grade()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def get_last_name(record):
    return record[1][1]

def display_by_last_name():
    sorted_records = sorted(records, key=get_last_name)
    print("\nStudent Records (Ordered by Last Name):")
    print_records(sorted_records)

def compute_grade(record):
    return 0.6 * record[2] + 0.4 * record[3]

def display_by_grade():
    sorted_records = sorted(records, key=compute_grade, reverse=True)
    print("\nStudent Records (Ordered by Grade):")
    print_records(sorted_records)

def print_records(record_list):
    print("ID\t\tName\t\t\tClass Standing\t\tExam")
    print("-" * 80)
    for record in record_list:
        print(f"{record[0]}\t\t{record[1][0]} {record[1][1]}\t\t{record[2]}\t\t\t{record[3]}")

def display_record():
    student_id = input("Enter Student ID: ")
    for record in records:
        if record[0] == student_id:
            print("\nStudent Record:")
            print("ID\t\tName\t\t\tClass Standing\t\tExam")
            print("-" * 80)
            print(f"{record[0]}\t\t{record[1][0]} {record[1][1]}\t\t{record[2]}\t\t\t{record[3]}")
            return
    print("Student not found.")

def add_record():
    print("\nAdd New Record:")
    student_id = input("Enter Student ID (6 digits): ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID. Must be 6 digits.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Student record added successfully.")

def edit_record():
    student_id = input("Enter Student ID to Edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            print("\nEdit Record:")
            first_name = input(f"Enter New First Name ({record[1][0]}): ") or record[1][0]
            last_name = input(f"Enter New Last Name ({record[1][1]}): ") or record[1][1]
            class_standing = float(input(f"Enter New Class Standing Grade ({record[2]}): ") or record[2])
            major_exam = float(input(f"Enter New Major Exam Grade ({record[3]}): ") or record[3])
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Student record updated successfully.")
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter Student ID to Delete: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Student record deleted successfully.")
            return
    print("Student not found.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Display All Records")
        print("5. Display Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        choice = input("Enter your choice (number): ")
        if choice == '1':
            open_file()
        elif choice == '2':
            save_records()
        elif choice == '3':
            save_as_records()
        elif choice == '4':
            display_all_records()
        elif choice == '5':
            display_record()
        elif choice == '6':
            add_record()
        elif choice == '7':
            edit_record()
        elif choice == '8':
            delete_record()
        elif choice == '9':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
