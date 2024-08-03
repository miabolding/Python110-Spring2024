# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   MBolding,7/31/2024,Created Script
#   MBolding, 8/2/2024, Add user input error handling
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
import json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Import TextIO from typing module
from typing import TextIO

# Define Constants
FILE_NAME: str = "Enrollments.json"

# Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str, str] = {}  # One row of student data
students: list[dict[str, str]] = []  # A table of student data
file: TextIO = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Holds the choice made by the user.
parts: list[str]  # Holds parts of the split CSV line

# When the program starts, read the file data into a list of dictionaries
try:
    with open(FILE_NAME, "r") as file:
        for row in file.readlines():
            # Transform the data from the file
            parts = row.strip().split(',')
            student_first_name = parts[0]
            student_last_name = parts[1]
            course_name = parts[2]
            # Setting up keys
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            # Load it into our collection (list of dictionaries)
            students.append(student_data)
except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# print(students) hide this so there no long string at the begining of program.

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Read above option and select what would you like to do: ")

    # MENU 1: Register a student
    if menu_choice == "1":
        student_first_name = input("Enter the student's first name: ")
        if not student_first_name.isapha():
            raise ValueError('First name must be alphabetic')
        student_last_name = input("Enter the student's last name: ")
        if not student_last_name.isapha():
            raise ValueError('Last name must be alphabetic')
        course_name = input("Please enter the name of the course: ")
        if not course_name.isalnum():
            raise ValueError('course name must be alphanumeric')
        student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
        students.append(student_data)
        continue

    # MENU 2: Show current data
    elif menu_choice == "2":
        # Print the header row
        print("-" * 50)
        # Convert the list of students dictionaries to a JSON formatted string
        json_data = json.dumps(students, indent=4)
        # Print the JSON formatted data
        print(json_data)
        print("-" * 50)
        continue

    # Menu 3: Save data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=1)
        except AttributeError as e:
            print(e, e.__doc__)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
        continue

    # Menu 4: Exit the program
    elif menu_choice == "4":
        print("Leaving Program.")
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")