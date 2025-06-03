# Simple Calculator

A basic calculator program that performs fundamental arithmetic operations.

## Description

This calculator performs basic mathematical operations including addition, subtraction, division, and multiplication. It features a modular design with separate functions for each operation.

## How to Use

1. Run the program: `python main.py`
2. Enter the first number when prompted
3. Enter the second number when prompted
4. Choose an operation by entering the corresponding number:
   - 1 for Addition
   - 2 for Subtraction
   - 3 for Division
   - 4 for Multiplication
5. View the calculated result

## Supported Operations

- **Addition**: Adds two numbers
- **Subtraction**: Subtracts the second number from the first
- **Division**: Divides the first number by the second (with zero-division protection)
- **Multiplication**: Multiplies two numbers

## Features

- Modular function-based design
- Error handling for division by zero
- Clean user interface
- Input validation
- Comprehensive operation menu

## Safety Features

- **Division by Zero Protection**: Returns error message instead of crashing
- **Invalid Option Handling**: Alerts user for invalid operation choices

## Learning Concepts

- Function definition and calling
- Dictionary data structures
- Error handling and validation
- Modular programming design
- Mathematical operations
- User input processing

## Code Structure

- Individual functions for each mathematical operation
- Main calculator function using operation dictionary
- User interface and input handling
- Error prevention and validation

## How to Run

```bash
python main.py
```

## Example Usage

```
Enter num1: 10
Enter num2: 5
Choose operation:
1. Add    2. Subtract
3. Divide 4. Multiply
Operation Choice: 1
Result: 15
```

## Requirements

- Python 3.6 or higher

## Educational Purpose

This program demonstrates:
- Function-based programming
- Dictionary usage for operation mapping
- Error handling best practices
- User interface design
- Mathematical operation implementation

## Potential Enhancements

- Add more advanced operations (exponents, square root)
- Implement calculation history
- Add decimal precision control
- Create graphical user interface
- Support for complex numbers
