# 🎓 Student Marks Validator

A simple Python mini project that validates student marks using **exception handling** and **custom errors**.

## 📌 About the Project

The Student Marks Validator is a beginner-friendly Python program that asks the user to enter student marks.

The program checks whether the entered marks are within the valid range of **0 to 100**.

It also handles unexpected errors using Python's `try-except` mechanism.

## 🎯 Purpose

The main purpose of this project is to practice:

- Exception Handling
- `try` block
- `except` block
- `Exception as e`
- `raise` keyword
- `ValueError`
- Input validation
- Custom error messages

## 🛠️ Technologies Used

- Python
- Python Exception Handling
- Python `raise` keyword

## 💻 Program

```python
try:
    print("===== Student Marks Validator =====")

    marks = int(input("Enter the marks : "))

    if marks < 0 or marks > 100:
        raise ValueError("Error: Marks should be between 0 and 100.")

    print("Valid marks!")

except Exception as e:
    print(e)
🔍 How It Works
1. Taking Input

The program asks the user to enter student marks.

marks = int(input("Enter the marks : "))

The input is converted into an integer.

2. Validating Marks

The program checks whether the marks are between 0 and 100.

if marks < 0 or marks > 100:
    raise ValueError("Error: Marks should be between 0 and 100.")

If the marks are outside the valid range, the program intentionally raises a ValueError.

3. Handling Exceptions

The except block catches the exception.

except Exception as e:
    print(e)

Using Exception as e allows the program to store the error inside e and print the error message.

📊 Example Outputs
✅ Valid Input
===== Student Marks Validator =====
Enter the marks : 85
Valid marks!
❌ Marks Greater Than 100
===== Student Marks Validator =====
Enter the marks : 120
Error: Marks should be between 0 and 100.
❌ Negative Marks
===== Student Marks Validator =====
Enter the marks : -10
Error: Marks should be between 0 and 100.
❌ Invalid Input
===== Student Marks Validator =====
Enter the marks : ABC
invalid literal for int() with base 10: 'ABC'
🧠 Concepts Learned
try

The try block contains code that might produce an exception.

except

The except block handles the exception so that the program does not terminate unexpectedly.

raise

The raise keyword is used when the programmer intentionally wants to create an exception.

Exception as e

It stores the exception object in the variable e.

except Exception as e:
    print(e)

This allows us to display the actual error message.

🌟 Key Learning

This project helped me understand the difference between:

Python automatically raising an error

and

A programmer intentionally raising an error.

For example:

raise ValueError("Error: Marks should be between 0 and 100.")

Here, the programmer intentionally raises the error because marks outside the range are not acceptable.

🚀 Future Improvements

This project can be improved by adding:

Student name
Multiple students
Grade calculation
Percentage calculation
Pass/Fail status
Menu-driven system
Multiple subject marks
File storage
Student result report
👩‍💻 Author

Akshata

Computer Science Engineering Student

Learning Python and preparing for placements.

📚 Learning Progress

This project was created while learning Python Exception Handling.

Topics practiced:

Try-Except
Finally
Raise
ValueError
Custom Error Messages
Input Validation