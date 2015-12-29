import math

def function(x):
    return x**2 + 2*x + 16

def dihotom(a, b, e = 1e-3):
    while abs(a-b) >= e:
        x = (a+b)/2
        f1 = function(x - e)
        f2 = function(x + e)
        if f1 < f2:
            b = x
        else:
            a = x
    x = (a+b)/2
    print("x", x)
    return function(x)


# x -0.9999999693135504
# 15.0
def gold(a, b, e = 1e-10):
    T1 = 0.381966
    T2 = 1 - T1
    while abs(a-b) >= e:
        x1 = a + (b - a) * T1
        x2 = a + (b - a) * T2
        f1 = function(x1)
        f2 = function(x2)
        if f1 < f2:
            b = x2
            x2 = x1
        else:
            a = x1
            x1 = x2
    x = (a + b)/2
    print("x", x)
    return function(x)

def fib_min(a, b, e = 1e-10):
    n = math.ceil((b - a)/e)
    s = 1
    while fib(s) < n:
        s += 1
    l = (b - a)/fib(s)
    x1 = a + l * fib(s - 2)
    x2 = b - l * fib(s - 2)
    i = 1
    while i < s:
        if function(x1) > function(x2):
            a = x1
            x1 = x2
            x2 = b - l * fib(s - 2 - i)
        else:
            b = x2
            x2 = x1
            x1 = a + l * fib(s - 2 - i)
        i += 1
    x = (x1 + x2)/2
    print(x)
    return function(x)
        


def fib(n):
    a = 1
    b = 1
    c = 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c

print(gold(-3, 5))
print(fib_min(-3, 5))
