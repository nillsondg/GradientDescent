import math
import timeit

#def function(x):
#    return x**2 + 2*x + 16

# time 0.02201113149373407
# time 0.021866441887461008
# x -0.9999954104059725
# 15.000000000021064
def dihotom(a, b, e = 1e-10):
    t = timeit.Timer()
    while abs(a-b) >= e:
        x = (a+b)/2
        f1 = function(x - e)
        f2 = function(x + e)
        if f1 < f2:
            b = x
        else:
            a = x
    print(t.timeit())
    x = (a+b)/2
    print("x", x)
    return function(x)

# time 0.022031844321190874
# time 0.022017435397742702
# x -0.9999999693135504
# 15.0
def gold(a, b, e = 1e-10):
    t = timeit.Timer()
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
    print(t.timeit())
    x = (a + b)/2
    print("x", x)
    return function(x)

