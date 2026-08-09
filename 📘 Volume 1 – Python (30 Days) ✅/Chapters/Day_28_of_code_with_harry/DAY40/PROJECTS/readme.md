# 🔐 Coding & Decoding Program

A simple Python mini project that allows users to **encode and decode words** using a custom coding and decoding logic.

## 📌 About the Project

This project is a menu-driven Python program with three options:

1. Coding
2. Decoding
3. Exit

The program uses **functions, loops, conditional statements, exception handling, and custom exceptions** to perform the operations.

## 🎯 Purpose

The main purpose of this project is to practice:

- Python Functions
- `while` loop
- `if-elif-else`
- String manipulation
- String slicing
- `try-except`
- `raise` keyword
- `ValueError`
- `IndexError`
- Input validation
- Custom error messages
- Menu-driven programs

## 🛠️ Technologies Used

- Python
- Python Exception Handling
- Python String Operations

## ⚙️ How the Program Works

### 🔹 Coding

If the input contains **3 or more characters**:

1. The first character is moved to the end.
2. `aks` is added at the beginning.
3. `san` is added at the end.

Example:

```text
Input: hello
Output: aksehllosan
````

If the input contains fewer than 3 characters, the first character is moved to the end.

### 🔹 Decoding

For a coded word:

1. The first 3 characters are removed.
2. The last 3 characters are removed.
3. The last character is moved to the beginning.

This restores the original word.

## 🚨 Error Handling

The program handles different invalid inputs.

### Empty Input

If the user enters an empty string:

```text
You can't use empty string
```

An `IndexError` is raised.

### Restricted Words

The words `abc` and `san` are not allowed.

A `ValueError` is raised for these inputs.

### Invalid Menu Option

If the user enters something other than options `1`, `2`, or `3`, the program displays:

```text
Invalid option
```

### Invalid Menu Input

If the user enters a non-integer value for the menu option, the program handles the `ValueError` and displays:

```text
ValueError! Please enter a number.
```

## 💻 Main Concepts Used

```python
try:
    # Risky code
except Exception as e:
    print(e)
```

Custom errors are raised using:

```python
raise ValueError("Custom error message")
```

## 📂 Project Structure

```text
Coding-Decoding/
│
├── coding_decoding.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python coding_decoding.py
```

## 📋 Menu

```text
========== WELCOME TO CODING WORLD ==========

1. CODING
2. DECODING
3. EXIT
```

## 📚 What I Learned

Through this project, I practiced how to:

* Create and call functions
* Work with strings
* Use string indexing and slicing
* Build menu-driven applications
* Use `while` loops
* Validate user input
* Handle exceptions
* Raise custom exceptions
* Display meaningful error messages

## 👩‍💻 Author

**Akshata**

Computer Science Engineering Student

This project was created as part of my Python learning and placement preparation journey.

```
```
