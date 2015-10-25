# x^2 + 9*y^2 - 2*x*y^(1/2) - 3*x - 26*y + 6*y^(1/2) + 16

def function(x):
    return x[0]**2 + 9*x[1]**2 - 2*x[0]*x[1]**(1/2) - 3*x[0] - 26*x[1] + 6*x[1]**(1/2) + 16
#derivative
def derX(x):
    return 2*x[0] + 2*x[1]**(1/2) - 3
def derY(x):
    return 18*x[1] - x[0]*x[1]**(-1/2) - 26 + 3*x[1]**(-1/2)
def grad(x):
    return [derX(x), derY(x)]
def derXX(x):
    return 2
def derXY(x):
    return x[1]**(-1/2)
def derYY(x):
    return 18 + x[0]*x[1]**(-3/2) - 1.5*x[1]**(-3/2)
