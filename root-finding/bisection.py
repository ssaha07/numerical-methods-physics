#The bisection method is based on the Intermediate Value Theorem, which states that if f(x) is a continuous function on the 
#interval [a, b] and f(a) and f(b) have opposite signs (i.e., f(a)⋅f(b) < 0), then there is at least one root of the equation , c
#for which f(c) = 0 in the interval (a,b).
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

N = 100
def bisection(f, low, high, tol = 1e-5):
    a = low
    b = high
    c = (a + b) / 2
    if (f(a) * f(b) >= 0):
        print("Root maynot exist within this interval.")
        return

    iterations=[]
    errors=[]
    print("---- BISECTION METHOD ----\n")
    print(f"{'n':<5}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}")
    print('-' * 53)
    n = 1
    while(n <= N):
        c = (a + b) / 2
        fc = f(c)
        iterations.append(n)
        errors.append(fc)
        print(f"{n:<5}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}")

        if(abs(fc) < tol or (abs(b - a) / 2) < tol):
            print("Root = ", c)
            print("Iterations = ", n)
            return
        if(f(a) * fc < 0):
            b = c
        else:
            a = c
        n = n + 1
    print("Approximate root = ", (a + b) / 2)

    plt.figure()
    plt.plot(iterations, errors, marker = 'o')
    plt.xlabel("ITERATIONS")
    plt.ylabel("|f(c)|")
    plt.yscale("log")
    plt.title("CONVERGENCE OF BISECTION METHOD")
    plt.grid(True)
    plt.show()
    