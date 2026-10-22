# Darkice60
# fast_ft file for fourier-analysis

#import math and cmath
import math
import cmath

# function for FFT
def fft(values):
    # set n equal to the number of values
    n = len(values)
    # if the length is one or below
    if n <= 1:
        # return values
        return values
    # recursively call FFT by splitting values into even and odd
    even = fft(values[0::2])
    odd = fft(values[1::2])

    # result length is n
    result = [0j] * n
    # for k in range n/2 - 1
    for k in range(n // 2):
        # calc the twiddle factor
        twiddle = cmath.exp(-2j * math.pi * k / n)
        # at index k, result equals even + twiddle * odd
        result[k] = even[k] + twiddle * odd[k]
        # at index k + n // 2, result equals even - twiddle * odd
        result[k + n // 2] = even[k] - twiddle * odd[k]
    # return the result
    return result