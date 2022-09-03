import numpy as np

def simps(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must be an integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


lower_limit = float(input("Enter the lower integral limit: "))
upper_limit = float(input("Enter the upper integral limit: "))

sub_interval = int(input("Enter the number of intervals: "))

f = lambda x: eval(input("Enter the function: "))

print(simps(f,lower_limit,upper_limit,sub_interval))