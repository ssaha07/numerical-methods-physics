#newton-raphson: an iterative method used to find isolated roots of an equation f(x) = 0. Initially, a crude approximation small 
#interval of [a, b] is found in which a only one root c(say) exists for which f(c) = 0.
#assumptions : f(a) . f(b) < 0, then x_0 = a and x_(n + 1) = x_n + h
#where h = small correction on x_0 = - [f(c) / f'(c)]

import sympy as sp
import matplotlib.pyplot as plt
N = 100
def newton_raphson(f_expr, low, high, tol = 1e-5):
    a = low
    b = high
    
    iterations = []
    errors = []
    print("---- NEWTON-RAPHSON METHOD ----\n")
    x = sp.symbols('x')
    df_expr = sp.diff(f_expr, x)
    f = sp.lambdify(x, f_expr, 'math')
    df = sp.lambdify(x, df_expr, 'math')
    if((f(a) * f(b)) >= 0):
        print("Root doesnot exists within this interval")
        return
    print(f"{'n':<5}{'x_n':<12}{'f(x_n)':<12}{'f′(xₙ)':<12}{'h':<12}{'xₙ₊₁':<12}")


    print('-' * 63)
    n = 1
    x_n = (a + b) / 2
    while(n <= N):
        
        fx_n = f(x_n)
        dx_n = df(x_n)
        if(dx_n == 0):
            print("Derivative zero. Method fails.")
            return
        h = -(fx_n / dx_n)
        x_next = x_n + h

        iterations.append(n)
        errors.append(fx_n)

        print(f"{n:<5}{x_n:<12.6f}{fx_n:<12.6f}{dx_n:<12.6f}{h:<12.6f}{x_next:12.6f}")
        if(abs(x_next - x_n) <= tol):
            print("\nRoot = ", x_n)
            print("Iterations = ", n)
            return
        n = n + 1
        x_n = x_next

    plt.figure()
    plt.plot(iterations, errors, marker='o')
    plt.xlabel("|f(x_n)|")
    plt.ylabel("Iterations")
    plt.yscale("log")
    plt.title("Convergence of Newton-Raphson Method")
    plt.grid(True)
    plt.show()



   

   

    