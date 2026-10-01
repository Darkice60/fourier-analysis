# Darkice60
# discrete_ft file for fourier-analysis

import math
import cmath

def dft(values):
    result = []
    n_tot = len(values)
    for k in range(n_tot):
        value = 0j
        for n in range(n_tot):
            value += values[n] * cmath.exp(-2j * math.pi * k * n * (1/n_tot))
        result.append(value)
    return result

def create_val():
    values = []
    i = 0
    while True:
        val = ""
        val = input(f"Enter x_{i}:\n")
        if (val.casefold() == "done"):
            break
        values.append(float(val))
        i += 1
    return values