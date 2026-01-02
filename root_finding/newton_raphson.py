#newton-raphson: an iterative method used to find isolated roots of an equation f(x) = 0. Initially, a crude approximation small 
#interval of [a, b] is found in which a only one root c(say) exists for which f(c) = 0.
#assumptions : f(a) . f(b) < 0, then x_0 = a and x_(n + 1) = x_n + h
#where h = small correction on x_0 = - [f(c) / f'(c)]

import sympy as sp
import numpy as np

N = 100
def newton_raphson(f_expr, low, tol = 1e-5):
    a = low
    
    
    iterations = []
    x_vals=[]
    h_vals=[]
    errors = []
    
    x = sp.symbols('x')
    df_expr = sp.diff(f_expr, x)
    f = sp.lambdify(x, f_expr, 'numpy')
    df = sp.lambdify(x, df_expr, 'numpy')
    
    



    n = 1
    x_n = a
    while(n <= N):
        
        fx_n = f(x_n)
        dx_n = df(x_n)
        if(dx_n == 0):
            raise ZeroDivisionError("Derivative is zero")
        if(abs(dx_n) < 1e-10):
            raise ZeroDivisionError("Derivative too small")
        h = -(fx_n / dx_n)
        x_next = x_n + h

        iterations.append(n)
        x_vals.append(x_n)
        h_vals.append(h)
        errors.append(abs(fx_n))

        
        if(abs(h) <= tol):
            return x_next, x_vals, h_vals, iterations, errors
        n = n + 1
        x_n = x_next
    return x_n, x_vals, h_vals, iterations,  errors

  



   

   

    