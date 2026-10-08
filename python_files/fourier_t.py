# Darkice60
# ft file for fourier-analysis

# import math and cmath for functions
import math
import cmath
# import numpy for a loop range
import numpy as np

# function for the value of the continous fourier transform at a specfic xi
def fourier_transform(f, xi, t, n):
    # calc the change in time
    delta_t = (2*t)/(n-1)
    # set the default FT value to 0 * j
    value = 0j
    # loop for integran approximation with riemann sum at desired resolution n
    for i in range(math.ceil(n)):
        # calc the x value (interates throug from -t to t depending on the current loop iteration)
        x = -t + i * delta_t
        # add the integral value to the value
        value += f(x) * cmath.exp(-1j * 2 * math.pi * xi * x) * delta_t
    # return the value (the FT integral)
    return value

# function to create a mathematical function
def create_func(func_string):
    # function that represents an f(x)
    def f(x):
        # create the fucntion using a string and eval
        func = eval(func_string, {"x": x, "math": math, "cmath": cmath})
        # return the eval
        return func
    # return the mathematical function
    return f

## below is for frequency finding

# finds (coarsely) the frequencies present in a function in a certain frequency range
# uses CFT for this
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

#
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