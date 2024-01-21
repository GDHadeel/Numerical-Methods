
# Euler Method
# Hadeel Balahmar-Shumokh Abdullah
# 25-May-2023
import math
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, n):
    """
    Solves an initial value problem using Euler's method.

    Parameters:
    - f: The function defining the differential equation dy/dx = f(x, y).
    - x0: The initial value of x.
    - y0: The initial value of y at x = x0.
    - h: The step size.
    - n: The number of steps to take.

    Returns:
    - x: A list of x-values.
    - y: A list of corresponding y-values.
    """
    x = [x0]
    y = [y0]

    for i in range(n):
        xi = x[i]
        yi = y[i]
        xi_plus_1 = xi + h
        f_func = lambda x, y: eval(f)  # Create dynamic function using lambda
        yi_plus_1 = yi + h * f_func(xi, yi)
        x.append(xi_plus_1)
        y.append(yi_plus_1)

    return x, y

try:
    # User input for the function f
    function_input = input("Enter the function f(x, y): ")
    f = function_input.replace('^', '**').replace('e', 'math.e').replace('sin', 'math.sin').replace('cos', 'math.cos').replace('exp', 'math.exp')

    # User input for other parameters
    x0 = float(input("Enter the initial value of x: "))
    y0 = float(input("Enter the initial value of y at x = x0: "))
    h = float(input("Enter the step size: "))
    n = int(input("Enter the number of steps: "))

    x_values, y_values = euler_method(f, x0, y0, h, n)

    # Print the results
    for i in range(len(x_values)):
        print(f"x = {x_values[i]}, y = {y_values[i]}")

    # Plotting the points on a graph
    plt.plot(x_values, y_values, '-o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Euler's Method")
    plt.show()

except:
    print("Invalid input. Please make sure you have entered the correct values.")
