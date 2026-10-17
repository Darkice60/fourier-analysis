# Darkice60
# fast_ft file for fourier-analysis

import math
import cmath

def fft(values):
    n = len(values)

    if n <= 1:
        return values

    even = fft(values[0::2])
    odd = fft(values[1::2])

    result = [0j] * n
    for k in range(n // 2):
        twiddle = cmath.exp(-2j * math.pi * k / n)
        result[k] = even[k] + twiddle * odd[k]
        result[k + n // 2] = even[k] - twiddle * odd[k]
    return result