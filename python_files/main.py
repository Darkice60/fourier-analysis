# Darkice60
# main file for fourier-analysis

import math
import cmath
import numpy as np

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

def find_high(xi_min, xi_max):
    results = []
    peaks = []
    for xi in np.arange(xi_min, xi_max, 0.05):
                f_hat = fourier_transform(func, xi, t, n)
                results.append((xi, f_hat, abs(f_hat)))
    for i in range(1, len(results) -1):
        _, _, magnitude_before = results[i - 1]
        xi, f_hat, magnitude = results[i]
        _, _, magnitude_after = results[i + 1]
        if magnitude_before < magnitude and magnitude > magnitude_after:
            peaks.append((xi, f_hat, magnitude))
    return peaks


choice = 2
dest = False

while not dest:
    func_string = input("Enter your function. \"USE CMATH FOR FUNCTIONS\"\n")
    func = create_func(func_string)
    if choice == 1:
        xi = float(input("xi value?\n"))
        t = float(input("integration domain? \"(make it so that the function decays to zero fast enough so that the domain to infinity is insignificant)\"\n"))
        n = float(input("number of steps?\n"))
        f_hat = fourier_transform(func, xi, t, n)
        print(f_hat)
    elif choice == 2:
        t = float(input("integration domain?\n"))
        n = float(input("number of steps?\n"))
        xi_min = float(input("what is the lowest frequency you would like to search for?\n"))
        xi_max = float(input("what is the highest frequency you would like to search for?\n"))
        peaks = find_high(xi_min, xi_max)

    dest = bool(input("End?\n"))