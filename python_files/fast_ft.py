# Darkice60
# fast_ft file for fourier-analysis

import math
import cmath

def fft(values):
    result = []
    n_tot = len(values)
    for k in range(n_tot):
        value1 = 0j
        value2 = 0j
        for m in range(math.ceil(n_tot/2 -1)):
            value1 += values[2 * m] * cmath.exp(-2j * math.pi * k * 2 * m * (1/n_tot))
            value2 += values[2 * m + 1] * cmath.exp(-2j * math.pi * k * (2 * m + 1) * (1/n_tot))
        result.append(value1 + value2)
    return result