import math
from root_finding import bisection, newton_raphson

def f(x):
    return x - math.tan(x)
    #return x - math.exp(x)
    #return x - math.log(x)

def main():
    print("NUMERICAL SOLUTION OF A TRANSCENDENTAL EQUATION")
    print("Equation 1 : x = tan(x)\n")
    #print("Equation 2 : x = e^(x)\n")
    #print("Equation 2 : x = ln (x)\n")
    a, b = 1.5, 2.0
    # ---- Bisection Method ----
    
    bisection(f, a, b)
    
    # ---- Newton-Raphson Method ----
    
    #newton_raphson(f, a, b)
    

# Entry point
if __name__ == "__main__":
    main()