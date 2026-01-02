import math
import sympy as sp
from root_finding import bisection, newton_raphson
import matplotlib.pyplot as plt
def f(x):
    return x - math.tan(x)
    #return x - math.exp(x)
    #return x - math.log(x)


def main():
    print("NUMERICAL SOLUTION OF A TRANSCENDENTAL EQUATION")
    print("Equation 1 : x = tan(x)\n")
    #print("Equation 2 : x = e^(x)\n")
    #print("Equation 2 : x = ln (x)\n")
    a, b = 1.0, 2.0
    # ---- Bisection Method ----
    print("---------BISECTION METHOD-----------")
    root_bi, cval_bi, iterations_bi, errors_bi = bisection(f, a, b)
    print(f"{'n':<5}{'c = (a + b) / 2':<12}{'f(c)':<12}")
    print('-' * 53)
    for i in range(len(iterations_bi)):
        print(f"{iterations_bi[i]:<5d}{cval_bi[i]:<12.6f}{errors_bi[i]:<12.6f}")
    print(f"Root of the equation: {root_bi:<12.6f}")
    plt.figure()
    plt.plot(iterations_bi, errors_bi, marker = 'o')
    plt.xlabel("Iterations")
    plt.ylabel("|f(c)|")
    plt.yscale("log")
    plt.title("Convergence of Bisection Method")
    plt.grid(True)
    plt.savefig("Bisection_convergence.png", dpi=300, bbox_inches="tight")

    
    # ---- Newton-Raphson Method ----
    print("---------NEWTON-RAPHSON METHOD--------")
    x = sp.symbols('x')
    f_expr = x - sp.tan(x)
    #f_expr = x - sp.exp(x)
    #f_expr = x - sp.log(x)
    root_nr, cvals_nr, hvals_nr, iterations_nr, errors_nr = newton_raphson(f_expr, 4.5)
    print(f"{'n':<5}{'x_n':<12}{'h_n':<12}{'|f(x_n)|':<12}")
    print('-' * 53)
    for i in range(len(iterations_nr)):
        print(f"{iterations_nr[i]:<5d}{cvals_nr[i]:<12.6f}{hvals_nr[i]:<12.6f}{errors_nr[i]:<12.6f}")
    print(f"Root of the equation: {root_nr:<12.6f}")
    plt.figure()
    plt.plot(iterations_nr, errors_nr, marker = 'o')
    plt.xlabel("Iterations")
    plt.ylabel("|f(x_n)|")
    plt.yscale("log")
    plt.title("Convergence of Netwon-Raphson Method")
    plt.grid(True)
    plt.savefig("NewtonRaphson_convergence.png", dpi=300, bbox_inches="tight")


# Entry point
if __name__ == "__main__":
    main()