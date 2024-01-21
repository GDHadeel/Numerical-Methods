
# Euler Method
# Hadeel Balahmar-Shumokh Abdullah
# 25-May-2023

import math
import matplotlib.pyplot as plt

def taylor_method(f, x0, y0, h, n):
    x = [x0]
    y = [y0]

    for i in range(n):
        xi = x[i]
        yi = y[i]
        xi_plus_1 = xi + h

        f_func = lambda x, y: eval(f)
        dy_dx = lambda x, y: (f_func(x + 0.0001, y) - f_func(x, y)) / 0.0001

        yi_plus_1 = yi + h * f_func(xi, yi) + (h ** 2) / 2 * dy_dx(xi, yi)
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

    x, y = taylor_method(f, x0, y0, h, n)

    # Print the results
    for i in range(len(x)):
        print(f"x = {x[i]}, y = {y[i]}")

    # Plotting the points on a graph
    plt.plot(x, y, '-o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Taylor Method")

    plt.show()

except:
    print("Invalid input. Please make sure you have entered the correct values.")
