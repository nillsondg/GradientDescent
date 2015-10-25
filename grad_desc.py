# x^2 + 9*y^2 - 2*x*y^(1/2) - 3*x - 26*y + 6*y^(1/2) + 16

import math

def function(x):
    return x[0]**2 + 9*x[1]**2 - 2*x[0]*x[1]**(1/2) - 3*x[0] - 26*x[1] + 6*x[1]**(1/2) + 16
#derivatives
def derX(x):
    return 2*x[0] - 2*x[1]**(1/2) - 3
def derY(x):
    return 18*x[1] - x[0]*x[1]**(-1/2) - 26 + 3*x[1]**(-1/2)
#gradient
def grad(x):
    return [derX(x), derY(x)]
##def derXX(x):
##    return 2
##def derXY(x):
##    return x[1]**(-1/2)
##def derYY(x):
##    return 18 + x[0]*x[1]**(-3/2) - 1.5*x[1]**(-3/2)

x_old = [0,0]
x_new = [3,7] # start
gamma = 0.01 # step size
precision = 0.00001

def absV(x_old, x_new):
    return math.sqrt((x_new[0] - x_old[0])**2 + (x_new[1] - x_old[1])**2)

while absV(x_old, x_new) > precision:
    x_old = x_new.copy()
    x_new[0] = x_old[0] - gamma * grad(x_old)[0]
    x_new[1] = x_old[1] - gamma * grad(x_old)[1]

print("Local minimum occurs at", x_new)
print("f =", function(x_new))
