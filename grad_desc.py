import math
# x^2 + 9*y^2 - 2*x*y^(1/2) - 3*x - 26*y + 6*y^(1/2) + 16
# f2 = (x - 3)^2 + 2 * ( y - 3)^2

from sympy import *

x, y = symbols('x y')
f = x**2 + 9*y**2 - 2*x*y**(1/2) - 3*x - 26*y + 6*y**(1/2) + 16
f2 = (x - 3)**2 + 2 * (y - 3)**2

n_digit = 5 # count of numbers 
x_start = (10, 10) # start
gamma = 5 # step size
precision = 10e-5

def absV(x_old, x_new):
    return math.sqrt((x_new[0] - x_old[0])**2 + (x_new[1] - x_old[1])**2)
    
def schet(f, x_start, precision, n_digit, verbose = False):

    #derivatives
    derX = diff(f, x)
    derY = diff(f, y)

    global gamma  #TODO remove dependency!
    x_old = [0,0]
    x_new = list(x_start)
    f_new = f.evalf(subs = {x:x_new[0], y:x_new[1]})
    if verbose == True:
        print("f start = ", round(f_new, n_digit))
        print("step size =", gamma)
    i = 1
    while absV(x_old, x_new) > precision:
        x_old = x_new.copy()
        f_old = f_new
        
        val_derX = derX.evalf(subs = {x:x_new[0], y:x_new[1]})
        val_derY = derY.evalf(subs = {x:x_new[0], y:x_new[1]})

        # move to new point by antigrad direction
        x_new[0] = x_old[0] - gamma * val_derX
        x_new[1] = x_old[1] - gamma * val_derY
        f_new = f.evalf(subs = {x:x_new[0], y:x_new[1]})
        
        i += 1
        if verbose == True:
            print("step =", i)
            print('grad = (', round(val_derX, n_digit), "; ", round(val_derY, n_digit), ")", sep="")
            print('x old = (', round(x_old[0], n_digit), "; ", round(x_old[1], n_digit), ")", sep="")
            print('x new = (', round(x_new[0], n_digit), "; ", round(x_new[1], n_digit), ")", sep="")
            if isinstance(f_new, Add): #is complex?
                print("f - complex")
            else:
                print("f =", round(f_new, n_digit))
        if(isinstance(f_new, Add) or f_old < f_new):
            gamma /= 2
            if verbose == True:
                print("change gamma = ", gamma)
                print("-" * 30)
            return -1
            print()

    print('point of minimum = (', round(x_old[0], n_digit), "; ", round(x_old[1], n_digit), ")", sep="")
    print("minimum f =", round(f.evalf(subs = {x:x_new[0], y:x_new[1]}), n_digit))
    return 1
    
while schet(f, x_start, precision, n_digit) == -1:
    pass
gamma = 5
while schet(f2, x_start, precision, n_digit) == -1:
    pass
