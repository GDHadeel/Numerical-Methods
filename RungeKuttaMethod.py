
# Runge-Kutta Method
# Hadeel Balahmar-Shumokh Abdullah
# 25-May-2023

import numpy as np
import matplotlib.pyplot as plt

try:
    # User input for the function f(t, y)
    function_input = input("Enter the function f(t, y): ")
    # Define the function based on user input
    def f_user(t, y):
        return eval(function_input.replace('^', '**').replace('e', 'np.e').replace('sin', 'np.sin').replace('cos', 'np.cos'))

    # User input for the initial condition and step size
    t0 = float(input("Enter the initial t value: "))
    y0 = float(input("Enter the initial y value: "))
    h = float(input("Enter the step size (h): "))

    # Define the number of steps to take
    n = round((1 - t0) / h)

    # Initialize arrays to store the solution
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0

    # Implement the RK4 method
    for i in range(n):
        k1 = h * f_user(t[i], y[i])
        k2 = h * f_user(t[i] + h/2, y[i] + k1/2)
        k3 = h * f_user(t[i] + h/2, y[i] + k2/2)
        k4 = h * f_user(t[i] + h, y[i] + k3)
        y[i+1] = y[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        t[i+1] = t[i] + h

    # Print the results in a table
    print(" i    |   t    |   y   ")
    print("-----------------------")
    for i in range(n+1):
        print(f"{i:2d}    |  {t[i]:.1f}  |  {y[i]:.6f}")

    # Plot the solution
    plt.plot(t, y, '-o')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Numerical Solution using RK4')
    plt.show()

except:
    print("Invalid input. Please make sure you have entered the correct values.")
