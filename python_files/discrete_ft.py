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

# create a list of wave values based on discrete points form the user
def create_val():
    # create a list of values and init an accumulator
    values = []
    i = 0
    # while not broken
    while True:
        # init value
        val = ""
        # ask the user for discrete value
        val = input(f"Enter x_{i}:\n")
        # if they type done, break the loop
        if (val.casefold() == "done"):
            break
        # append vale to the list after converting to float
        values.append(float(val))
        # add one to accumulator
        i += 1
    # return values list
    return values

# find the frequency values from the DFT
def find_frequencies(n_tot, delta_x):
    # change in frequency
    delta_xi = 1/(n_tot * delta_x)
    # list of frequencies
    freqs = []
    # iterate through the list
    for k in range(n_tot):
        # add the frequencies to the list
        if k <= n_tot // 2:
            freqs.append(k * delta_xi)
        else:
            freqs.append((k - n_tot) * delta_xi)
    # return the frequencies
    return freqs

# find the magnitudes of the DFT
def find_mags(n_tot, results):
    # create list of magnitudes
    mag = []
    # iterate through the DFT list
    for k in range(n_tot):
        # appened the magnitude
        mag.append(math.hypot(results[k].imag, results[k].real))
    # return the list of magnitudes
    return mag

# find the phase angles of the DFT
def find_angs(n_tot, results):
    # create a list of phase angles
    angs = []
    # iterate through the DFT list
    for k in range(n_tot):
        # if the DFT value is essentially 0
        if abs(results[k]) < 1e-12:
            # append None
            angs.append(None)
        else:
            # otherwise, appened the phase angle
            angs.append(math.atan2(results[k].imag, results[k].real))
    # return the list of phase angles
    return angs