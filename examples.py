from quadratic_solver import solve_quadratic

print("=" * 60)
print("QUADRATIC EQUATIONS - EXAMPLE PROBLEMS")
print("=" * 60)

# Example 1: Two real solutions
print("\n\nEXAMPLE 1: Two distinct real solutions")
print("-" * 60)
solve_quadratic(1, -5, 6)

# Example 2: One repeated solution
print("\n\nEXAMPLE 2: One repeated real solution")
print("-" * 60)
solve_quadratic(1, -2, 1)

# Example 3: Complex solutions
print("\n\nEXAMPLE 3: Complex solutions")
print("-" * 60)
solve_quadratic(1, 2, 2)

# Example 4: Your own example
print("\n\nEXAMPLE 4: Another problem")
print("-" * 60)
solve_quadratic(2, -7, 3)

print("\n" + "=" * 60)
print("End of Examples")
print("=" * 60)
