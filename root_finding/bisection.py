
#The bisection method is based on the Intermediate Value Theorem, which states that if f(x) is a continuous function on the 
#interval [a, b] and f(a) and f(b) have opposite signs (i.e., f(a)⋅f(b) < 0), then there is at least one root of the equation , c
#for which f(c) = 0 in the interval (a,b).




N = 100

def bisection(f, low, high, tol = 1e-5):
    a = low
    b = high
    c = (a + b) / 2
    if (f(a) * f(b) >= 0):
        raise ValueError("Invalid interval")

    iterations=[]
    c_values = []
    errors=[]
    
    n = 1
    while(n <= N):
        c = (a + b) / 2
        fc = f(c)
        iterations.append(n)
        c_values.append(c)
        errors.append(abs(fc))
        

        if(abs(fc) < tol or (abs(b - a) / 2) < tol):
            return c, c_values, iterations, errors
        if(f(a) * fc < 0):
            b = c
        else:
            a = c
        n = n + 1
    return c, c_values, iterations, errors

 
    