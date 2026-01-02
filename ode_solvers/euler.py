#euler-method: simple, single-step method for solving an ordinary initial-value
#differential equation.


def euler(f, x0, y0, h, N):
    x = x0
    y = y0
    res = [(x, y)]
    n=1
    while(n <= N):
        y = y + h * f(x, y)
        x = x + h
        res.append((x, y))
        
        n = n + 1
    return res
    