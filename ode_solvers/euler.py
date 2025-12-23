#euler-method: simple, single-step method for solving an ordinary initial-value
#differential equation.


def euler(f, x0, y0, h, N):
    x = x0
    y = y0
    res = [(x, y)]
    print(f"{'n':<5}{'x':<12}{'y':<12}")
    print('-' * 33)
    print(f"{0:<5}{x:<12}{y:<12}")
    n=1
    while(n <= N):
        y = y + h * f(x, y)
        x = x + h
        res.append((x, y))
        print(f"{n:<5}{x:<12.6f}{y:<12.6f}")
        n = n + 1
    return res
    