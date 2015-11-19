import math
# f = (x - 3)^2 + 2 * ( y - 3)^2

from sympy import *

x, y = symbols('x y')
f = (x - 3)**2 + 2 * (y - 3)**2
derX = diff(f, x)
derY = diff(f, y)

n_digit = 4 # count of numbers 
x_new = [10, 10] # start
gamma = 5 # step size
precision = 0.00001

def absV(x_old, x_new):
    return math.sqrt((x_new[0] - x_old[0])**2 + (x_new[1] - x_old[1])**2)
    
def schet():
    global n_digit
    global x_new
    global gamma
    global precision
    x_old = [0,0]
    f_new = f.evalf(subs = {x:x_new[0], y:x_new[1]})
    print("f start = ", round(f_new, n_digit))
    print("step size =", gamma)
    i = 1
    while absV(x_old, x_new) > precision:
        x_old = x_new.copy()
        f_old = f_new
        print("step =", i)
        val_derX = derX.evalf(subs = {x:x_new[0], y:x_new[1]})
        val_derY = derY.evalf(subs = {x:x_new[0], y:x_new[1]})
        print('grad = (', round(val_derX, n_digit), "; ", round(val_derY, n_digit), ")", sep="")
        print('x old = (', round(x_old[0], n_digit), "; ", round(x_old[1], n_digit), ")", sep="")
        i += 1
        x_new[0] = x_old[0] - gamma * val_derX
        x_new[1] = x_old[1] - gamma * val_derY
        f_new = f.evalf(subs = {x:x_new[0], y:x_new[1]})
        print('x new = (', round(x_new[0], n_digit), "; ", round(x_new[1], n_digit), ")", sep="")
        print("f =", round(f_new, n_digit))
        if(f_old < f_new):
            gamma /= 2
            print("change gamma = ", gamma)
            print("-" * 30)
            return -1
        print()

    print('point of minimum = (', round(x_old[0], n_digit), "; ", round(x_old[1], n_digit), ")", sep="")
    print("minimum f =", round(f.evalf(subs = {x:x_new[0], y:x_new[1]}), n_digit))
    return 1
    
while schet() == -1:
    pass
