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
    # create lists to do this, results is for the actual fourier transform values at each xi
    results = []
    # peaks is the list where the peaks of the CFT show up (top frequencies)
    peaks = []
    # create teh results list with 0.05 step
    for xi in np.arange(xi_min, xi_max, 0.05):
                # preform fouier transsform
                f_hat = fourier_transform(func, xi, t, n)
                # appened to results list
                results.append((xi, f_hat, abs(f_hat)))
    # get the actual peaks of the results out
    for i in range(1, len(results) -1):
        # get the magnitude one frequecncy value before and one after the test target
        _, _, magnitude_before = results[i - 1]
        xi, f_hat, magnitude = results[i]
        _, _, magnitude_after = results[i + 1]
        # if the test is greater than them both
        if magnitude_before < magnitude and magnitude > magnitude_after:
            # add the CFT info and frequcency to the peaks lits
            peaks.append((xi, f_hat, magnitude))
    # return the peaks list
    return peaks

# refines the actual peaks to find the frequencies
def refine_peaks(func, t, n, peaks):
    # list for the refined set of ferequiees
    refined = []
    # for the number of peaks
    for i in range(len(peaks)):
        # get the frequency and magnitude of teh CFT 
        xi, _, mag = peaks[i]
        # choose an arbitary step value size 
        step = 0.01 
        # while step is greater than 10^-10
        while step > 1e-10:  
            # get the siz eofd the peak slightly before and slightly after
            mag_before = abs(fourier_transform(func, (xi-step), t, n))
            mag_after = abs(fourier_transform(func, (xi+step), t, n))

            # if the magnitude before is greater than the magintude edit the frequecy value
            if mag_before > mag:
                xi -= step
                mag = mag_before
            # if the magnitude after is greater than the magintude edit the frequecy value
            elif mag_after > mag:
                xi += step
                mag = mag_after
                # otherwise divide by 10
            else:
                step /= 10
        # get the new CFT values
        f_hat = fourier_transform(func, xi, t, n)
        # add to the list
        refined.append((xi, f_hat, abs(f_hat)))\
    # return teh list
    return refined