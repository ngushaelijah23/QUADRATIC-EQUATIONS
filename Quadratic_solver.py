import math

def solve_quadratic(a, b, c):
    """
    Solve quadratic equation ax² + bx + c = 0
    """
    print(f"\nQuadratic Equation: {a}x² + {b}x + {c} = 0")
    
    # Step 1: Calculate discriminant
    discriminant = b**2 - 4*a*c
    print(f"\nStep 1: Calculate the discriminant")
    print(f"Δ = b² - 4ac")
    print(f"Δ = ({b})² - 4({a})({c})")
    print(f"Δ = {b**2} - {4*a*c} = {discriminant}")
    
    # Step 2: Determine type of solutions and calculate
    print(f"\nStep 2: Apply the quadratic formula")
    print(f"x = (-b ± √Δ) / 2a")
    
    if discriminant > 0:
        print(f"\nStep 3: Two distinct real solutions")
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"x₁ = ({-b} + √{discriminant}) / {2*a} = {x1}")
        print(f"x₂ = ({-b} - √{discriminant}) / {2*a} = {x2}")
        return x1, x2
    
    elif discriminant == 0:
        print(f"\nStep 3: One repeated real solution")
        x = -b / (2*a)
        print(f"x = {-b} / {2*a} = {x}")
        return x
    
    else:
        print(f"\nStep 3: Two complex conjugate solutions")
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        print(f"x₁ = {real_part} + {imag_part}i")
        print(f"x₂ = {real_part} - {imag_part}i")
        return complex(real_part, imag_part), complex(real_part, -imag_part)

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("QUADRATIC EQUATION SOLVER")
    print("=" * 50)
    
    try:
        a = float(input("\nEnter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        if a == 0:
            print("Error: Coefficient 'a' cannot be zero!")
        else:
            solutions = solve_quadratic(a, b, c)
            print(f"\n{'=' * 50}")
            print(f"Solutions: {solutions}")
            print(f"{'=' * 50}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
