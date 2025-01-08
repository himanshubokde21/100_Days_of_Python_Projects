import typing
from math import *

def Simpson(a: int, b: int, n: int, ex: str):
    y = []
    h = (b-a)/n
    idx = ex.index('x')
    
    # Generate all points
    for i in range(n+1):
        x = a + i * h
        y.append(round(eval(ex.replace(ex[idx], str(x))), 4))
    
    # Correct Simpson's 1/3 Rule Calculation
    fx = 0
    for i in range(len(y)):
        if i == 0 or i == len(y)-1:
            fx += y[i]  # First and last points weight 1
        elif i % 2 == 1:
            fx += 4 * y[i]  # Odd-indexed points weight 4
        else:
            fx += 2 * y[i]  # Even-indexed points weight 2
    
    # Final calculation
    result = round(h/3 * fx, 4)
    print("Simpson's 1/3rd: ", result)

a = int(input("start: "))
b = int(input("end: "))
n = int(input("intervers: "))
ex = input("F(x): ")
Simpson(a, b, n, ex)
