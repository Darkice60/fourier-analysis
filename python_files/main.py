# Darkice60
# main file for fourier-analysis

# import fouier_t for running code
import fourier_t as ft
import discrete_ft as dft
import sender as se
import receiver as re


dest = False

# while the user is not done
while not dest:
    # ask for chocie and init variable of if done or not
    choice = int(input("What would you like?\n1 - Fourier Transform at a frequency value?\n2 - Frequency finder using the Fourier Transform\n3 - Discrete Fourier Transform with Manual Input\n" \
    "4 - 'Send' a message using a signal as a wave.\n5 - Decode a 'signal' using the fourier transform.\nm"))

    # if the choice is is 1
    match choice:
        case 1:
            # ask user for function
            func_string = input("Enter your function. \"USE CMATH FOR FUNCTIONS\"\n")
            # convert to function
            func = ft.create_func(func_string)
            # ask user for frequency
            xi = float(input("xi value?\n"))
            # ask user for domain
            t = float(input("integration domain? \"(make it so that the function decays to zero fast enough so that the domain to infinity is insignificant)\"\n"))
            n = float(input("number of steps?\n"))
            f_hat = ft.fourier_transform(func, xi, t, n)
            mag = abs(f_hat)
            print(f"f̂(ξ) = {f_hat}, |f̂(ξ)| = {mag}")
        # if the choice is is 2
        case 2:
            # ask user for function
            func_string = input("Enter your function. \"USE CMATH FOR FUNCTIONS\"\n")
            # convert to function
            func = ft.create_func(func_string)
            # ask user for integration domain
            t = float(input("integration domain?\n"))
            # ask user for number of steps (resolution)
            n = float(input("number of steps?\n"))
            # ask user for frequency range
            xi_min = float(input("what is the lowest frequency you would like to search for?\n"))
            xi_max = float(input("what is the highest frequency you would like to search for?\n"))
            # find the highest freqencies coarsely
            peaks = ft.find_high(func, t, n, xi_min, xi_max)
            # find the highest peaks more precisely
            refined = ft.refine_peaks(func, t, n, peaks)
            # print out the frequencies, and their fourier transform values
            for i in range(len(refined)):
                xi, f_hat, mag = refined[i]
                print(f"ξ = {xi}, f̂(ξ) = {f_hat}, |f̂(ξ)| = {mag}")
        # if the choice is is 3
        case 3:
            # ask user for the spacing between samples
            delta_x = float(input("What is the difference in x?\n"))
            # ask user for values
            values = dft.create_val()
            # calc the results (DFT) from the user values
            results = dft.dft(values)
            # get the amt of bins
            n_total = len(results)
            # calc the freqencies, magnitudes, and angles from the DFT
            frequencies = dft.find_frequencies(n_total, delta_x)
            mags = dft.find_mags(n_total, results)
            angs = dft.find_angs(n_total, results)
            # print the DFT, Frequencies, Magnitudes, and Phase Angle for each bin
            print("Results:")
            for i in range(n_total):
                print(results[i])
            print("\nFrequencies:")
            for i in range(len(frequencies)):
                print(frequencies[i])
            print("\nMagnitudes:")
            for i in range(len(mags)):
                print(mags[i])
            print("\nPhase Angle:")
            for i in range(len(angs)):
                print(angs[i])
        # if the choice is is 4
        case 4:
            msg = input("Enter your message:\n")
            msg = msg.encode("utf-8")
            data = se.get_bytes(msg)
            bits = se.get_bits(data)
            signal = se.form_wave(bits)
            file_name = input("Enter the file to write to (fake medium):\n")
            se.write_file(file_name, signal)
            print(signal)
        # if the choice is is 5
        case 5:
            file_name = input("Enter the file to write to (fake medium):\n")
            signal = re.read_file(file_name)
            # bits = re.to_bits(signal, time_bit=0.1, sample_rate=0.1)
    dest = bool(input("End? (blank for no)\n"))