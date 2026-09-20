# Darkice60
# main file for fourier-analysis

import math
import cmath

def fourier_transform(f, xi, t, n):
    delta_t = (2*t)/(n-1)
    value = 0j
    
    for i in range(math.ceil(n)):
        x = -t + i * delta_t
        value += f(x) * cmath.exp(-1j * 2 * math.pi * xi * x) * delta_t
    return value

def create_func(func_string):
    def f(x):
        func = eval(func_string, {"x": x, "math": math, "cmath": cmath})
        return func
    return f

while True:
    func_string = input("Enter your function. \"USE CMATH FOR FUNCTIONS\"\n")
    func = create_func(func_string)
    xi = float(input("xi value?\n"))
    t = float(input("inetgration domain? \"(make it so that the function decays to zero fast enough so that the domain to infinity is insignificant)\"\n"))
    n = float(input("number of steps?\n"))
    f_hat = fourier_transform(func, xi, t, n)
    print(f_hat)