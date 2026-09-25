# Darkice60
# ft file for fourier-analysis

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

def find_high(func, t, n, xi_min, xi_max):
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

def refine_peaks(func, t, n, peaks):
    refined = []
    for i in range(len(peaks)):
        xi, _, mag = peaks[i]
        step = 0.01 
        while step > 1e-10:  
            mag_before = abs(fourier_transform(func, (xi-step), t, n))
            mag_after = abs(fourier_transform(func, (xi+step), t, n))

            if mag_before > mag:
                xi -= step
                mag = mag_before
            elif mag_after > mag:
                xi += step
                mag = mag_after
            else:
                step /= 10
        f_hat = fourier_transform(func, xi, t, n)
        refined.append((xi, f_hat, abs(f_hat)))
    return refined