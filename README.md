# Quadratic Equations Solver

A Python project to solve quadratic equations with step-by-step explanations and examples. 

## About This Project

This repository contains a Python program that solves quadratic equations in the form **ax² + bx + c = 0**. The solver uses the quadratic formula to find real and complex solutions and provides detailed step-by-step calculations.

## What Are Quadratic Equations?

A quadratic equation is a polynomial equation of the second degree. It has the general form:

```
ax² + bx + c = 0
```

Where:
- **a**, **b**, **c** are coefficients (with a ≠ 0)
- **x** is the variable we're solving for

### The Quadratic Formula

The solutions are found using the quadratic formula:

```
x = (-b ± √(b² - 4ac)) / 2a
```

The discriminant (Δ = b² - 4ac) determines the type of solutions:
- **Δ > 0**: Two distinct real solutions
- **Δ = 0**: One repeated real solution
- **Δ < 0**: Two complex conjugate solutions

## Features

✅ Solves quadratic equations using the quadratic formula  
✅ Displays step-by-step calculations  
✅ Handles real and complex solutions  
✅ Calculates the discriminant  
✅ Shows detailed results  
✅ Easy-to-use interface  

## Files in This Repository

- **quadratic_solver.py** - Main program with the solver function
- **examples.py** - Example problems with solutions
- **README.md** - Project documentation

## How to Use

### Installation

1. Make sure you have Python installed on your computer (Python 3.6+)
2. Clone or download this repository
3. Navigate to the project directory

### Running the Solver

```bash
python quadratic_solver.py
```

Then enter the coefficients when prompted:
```
Enter coefficient a: 1
Enter coefficient b: -5
Enter coefficient c: 6
```

### Running Examples

To see pre-solved example problems:

```bash
python examples.py
```

## Example Usage

**Problem:** Solve x² - 5x + 6 = 0

**Input:**
- a = 1
- b = -5
- c = 6

**Output:**
```
Quadratic Equation: x² - 5x + 6 = 0

Step 1: Calculate the discriminant
Δ = b² - 4ac
Δ = (-5)² - 4(1)(6)
Δ = 25 - 24 = 1

Step 2: Apply the quadratic formula
x = (-b ± √Δ) / 2a
x = (5 ± √1) / 2

Step 3: Calculate solutions
x₁ = (5 + 1) / 2 = 3
x₂ = (5 - 1) / 2 = 2

Solutions: x = 3 and x = 2
```

## What You'll Learn

- Understanding quadratic equations
- Using the quadratic formula
- Python functions and user input
- Handling mathematical calculations
- Working with real and complex numbers
- Problem-solving with code
- Step-by-step algorithm implementation

## Getting Started

If you're new to this project:
1. Start by reading this README to understand quadratic equations
2. Run `python examples.py` to see example problems
3. Run `python quadratic_solver.py` and try solving your own equations
4. Study the code to understand how it works

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Author

**ngushaelijah23**

## License

This project is licensed under the MIT License - feel free to use it for personal and educational purposes.

You are free to:
- Use this code for learning
- Modify the code
- Share the code with others
- Use it in your projects

## Contributing

Feel free to fork this repository, improve it, and share your improvements!

Feel free to fork, clone, or contribute to this repository! 

