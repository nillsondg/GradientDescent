import math
# x^2 + 9*y^2 - 2*x*y^(1/2) - 3*x - 26*y + 6*y^(1/2) + 16
# f2 = (x - 3)^2 + 2 * ( y - 3)^2

from sympy import *

x, y, z = symbols('x y z')
f3 = 2*x**2 + 4*x*y + 5*y**2 + 3*z**2

n_digit = 5 # count of numbers
x_start = (1, 1, 1) # start
gamma = 5 # step size
precision = 10e-6

def absA(x_old, x_new):
    s = 0
    for i in range(len(x_old)):
        s += (x_new[i] - x_old[i]) **2
    return math.sqrt(s)

def absV(x_old, x_new):
    return math.sqrt((x_new[0] - x_old[0])**2 + (x_new[1] - x_old[1])**2)
    
def schet(f, x_start, precision, n_digit, verbose = False):

    global gamma
    #derivatives
    derX = diff(f, x)
    derY = diff(f, y)
    derZ = diff(f, z)

    x_old = [0,0,0]
    x_new = list(x_start)
    f_new = f.evalf(subs = {x:x_new[0], y:x_new[1], z:x_new[2]})
    if verbose == True:
        print("f start = ", round(f_new, n_digit))
        print("step size =", gamma)
    i = 1
    while absV(x_old, x_new) > precision:
        x_old = x_new.copy()
        f_old = f_new
        
        val_derX = derX.evalf(subs = {x:x_new[0], y:x_new[1], z:x_new[2]})
        val_derY = derY.evalf(subs = {x:x_new[0], y:x_new[1], z:x_new[2]})
        val_derZ = derZ.evalf(subs = {x:x_new[0], y:x_new[1], z:x_new[2]})

        # move to new point by antigrad direction
        x_new[0] = x_old[0] - gamma * val_derX
        x_new[1] = x_old[1] - gamma * val_derY
        x_new[2] = x_old[2] - gamma * val_derZ
        f_new = f.evalf(subs = {x:x_new[0], y:x_new[1], z:x_new[2]})
        
        i += 1
        if verbose == True:
            print("step =", i)
            print('grad = (', round(val_derX, n_digit), "; ", round(val_derY, n_digit), "; ", round(val_derZ, n_digit), ")", sep="")
            print('x old = (', round(x_old[0], n_digit), "; ", round(x_old[1], n_digit), "; ", round(x_old[2], n_digit), ")", sep="")
            print('x new = (', round(x_new[0], n_digit), "; ", round(x_new[1], n_digit), "; ", round(x_new[2], n_digit), ")", sep="")
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

    print('point of minimum = (', round(x_old[0], n_digit), "; ", round(x_old[1], n_digit), "; ", round(x_old[2], n_digit), ")", sep="")
    print("minimum f =", round(f.evalf(subs = {x:x_new[0], y:x_new[1], z:x_new[2]}), n_digit))
    return 1

print("f =", f3)
print('x start = (', round(x_start[0], n_digit), "; ", round(x_start[1], n_digit), "; ", round(x_start[2], n_digit), ")", sep="")
while schet(f3, x_start, precision, n_digit, True) == -1:
    pass
