#Runge-kutta(order 4): A method to find the numerical solution of an ordinary differential equation
#with a greater accuracy, eliminating the need of calculating higher order differentiations.
#At each step:
# y_(n+1) = y_n + k where k = (k_1 + 2k_2 + 2k_3 + k4) / 6
# k_1 = hf(x_n, y_n)
# k_2 = hf(x_n + h/2, y_n + k_1/2)
# k_3 = hf(x_n + h/2, y_n + k_2/2)
# k_4 = hf((x_n + h), (y_n + k_3))

import sympy as sp
def runge_kutta(f, x0, y0, h, N):
    x = x0
    y = y0  
    res = [(x, y)]
    print(f"{'n':<5}{'x_n':<12}{'y_n':<12}{'k_1':<12}{'k_2':<12}{'k_3':<12}{'k_4':<12}{'k':<12}")
    print('-' * 73)
    n = 0
    while(n < N):
        k_1 = h * f(x, y)
        k_2 = h * f((x + h / 2), (y + k_1 / 2))
        k_3 = h * f((x + h / 2), (y + k_2 / 2))
        k_4 = h * f((x + h), (y + k_3))
        k = (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
        y_next = y + k
        
        print(f"{n:<5}{x:<12.6f}{y:<12.6f}{k_1:<12.6f}{k_2:<12.6f}{k_3:<12.6f}{k_4:<12.6f}{k:<12.6f}")
        
        x = x + h
        y = y_next
        res.append((x, y))
        n = n + 1
        
    return res

    
    