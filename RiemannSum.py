# Compute Riemann Sums for a given function on a given interval.
# 30 May 2024
# Author: 30 April 2024

import math as m

def safe_eval(expr, vars):
    """
    Evaluate a mathematical expression safely with given variables.
    """
    # Create a dictionary of allowed names from the math module
    allowed_names = {k: v for k, v in m.__dict__.items() if not k.startswith("__")}
    # Update the allowed names with user-provided variables
    allowed_names.update(vars)
    # Evaluate the expression using the allowed names
    return eval(expr, {"__builtins__": None}, allowed_names)

def calculate_riemann_sum(a, b, n, function, endpoint):
    """
    Calculate the Riemann sum for a given function over [a, b] with n rectangles.
    
    Parameters:
    a (float): The left endpoint of the interval.
    b (float): The right endpoint of the interval.
    n (int): The number of rectangles.
    function (str): The function to integrate, given as a string in terms of 'x'.
    endpoint (str): Specifies whether to use the left or right endpoint ('left' or 'right').
    
    Returns:
    float: The Riemann sum approximation of the integral.
    """
    # Calculate dx or 'delta x'
    dx = (b - a) / n
    # Initialize the sum
    total_sum = 0

    # Calculate the Riemann sum based on the chosen endpoint
    if endpoint == "left":
        for i in range(n):
            xi = a + i * dx  # xi = x_i
            total_sum += dx * safe_eval(function, {"x": xi})
    elif endpoint == "right":
        for i in range(1, n + 1):
            xi = a + i * dx
            total_sum += dx * safe_eval(function, {"x": xi})
    else:
        raise ValueError("Invalid endpoint choice. Please choose 'left' or 'right'.")

    return total_sum

def main():
    # Get user input for endpoints and the number of rectangles
    a = float(input("Enter the left endpoint: "))
    b = float(input("Enter the right endpoint: "))
    n = int(input("Enter the number of rectangles: "))

    # Get user input for the endpoint choice
    endpoint = input("Left or right endpoint: ").strip().lower()

    # Get user input for the function to integrate
    function = input("Enter the function in terms of x: ")

    # Calculate the Riemann sum
    try:
        sum_result = calculate_riemann_sum(a, b, n, function, endpoint)
        print("The Riemann sum is:", sum_result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
