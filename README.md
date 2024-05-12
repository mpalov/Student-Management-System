![image](https://github.com/mpalov/Student-Management-System/blob/main/Screenshots/sms_1.png)
![image](https://github.com/mpalov/Student-Management-System/blob/main/Screenshots/sms_2.png)
![image](https://github.com/mpalov/Student-Management-System/blob/main/Screenshots/sms_3.png)

# Student Management System

This is a simple Student Management System implemented using Python and CustomTkinter.

## Features

- Add new students with their information and grades.
- Update existing student records.
- Delete student records.
- Search for students by ID.
- View all student records in a table format.

## Prerequisites
- CustomTkinter library.
- CTkMessagebox

## Usage

- When you run the application, you'll see a GUI window for managing student records.
- Use the "Add" button to add new students and their grades.
- Use the "Update" button to update existing student records.
- Use the "Delete" button to delete student records.
- Use the "Search" button to search for students by ID.

## Technical Details

- The application is developed in Python 3.x using the CustomTkinter library for the graphical user interface.
- The data for student records is stored in-memory within the application. For production use, consider integrating a database backend.
- The GUI layout is designed using frames, labels, entry fields, dropdown menus, buttons, and a Treeview widget from Tkinter.
- Input validation is implemented to ensure that all required fields are filled before adding or updating student records.
- Error handling is included for scenarios such as empty fields or non-existent student or student IDs during deletion and updating.
