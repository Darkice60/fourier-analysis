# Darkice60
# discrete_ft file for fourier-analysis

# import math and cmath
import math
import cmath

# calculate the DFT from a set of wave values
def dft(values):
    # create a list for the results
    result = []
    # get the total amt of signal samples
    n_tot = len(values)
    # for all data samples
    for k in range(n_tot):
        # init a variable for the FFT value for each bin
        value = 0j
        # for the smaples given
        # calc the DFT value
        for n in range(n_tot):
            value += values[n] * cmath.exp(-2j * math.pi * k * n * (1/n_tot))
        # append the value to result
        result.append(value)
    # return the DFT
    return result

# 
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

def find_frequencies(n_tot, delta_x):
    delta_xi = 1/(n_tot * delta_x)
    freqs = []
    for k in range(n_tot):
        if k <= n_tot // 2:
            freqs.append(k * delta_xi)
        else:
            freqs.append((k - n_tot) * delta_xi)
    return freqs

def find_mags(n_tot, results):
    mag = []
    for k in range(n_tot):
        mag.append(math.hypot(results[k].imag, results[k].real))
    return mag

def find_angs(n_tot, results):
    angs = []
    for k in range(n_tot):
        if abs(results[k]) < 1e-12:
            angs.append(None)
        else:
            angs.append(math.atan2(results[k].imag, results[k].real))
    return angs