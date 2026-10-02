# Darkice60
# main file for fourier-analysis

# import fouier_t for running code
import fourier_t as ft
import discrete_ft as dft     

# ask for chocie and init variable of if done or not
choice = int(input("What would you like?\n1 - Fourier Transform at a frequency value?\n2 - Frequency finder using the Fourier Transform\n"))
dest = False

# while the user is not done
while not dest:
    # if the choice is is one
    if choice == 1:
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
    elif choice == 2:
        # ask user for function
        func_string = input("Enter your function. \"USE CMATH FOR FUNCTIONS\"\n")
        # convert to function
        func = ft.create_func(func_string)
        t = float(input("integration domain?\n"))
        n = float(input("number of steps?\n"))
        xi_min = float(input("what is the lowest frequency you would like to search for?\n"))
        xi_max = float(input("what is the highest frequency you would like to search for?\n"))
        peaks = ft.find_high(func, t, n, xi_min, xi_max)
        refined = ft.refine_peaks(func, t, n, peaks)
        for i in range(len(refined)):
            xi, f_hat, mag = refined[i]
            print(f"ξ = {xi}, f̂(ξ) = {f_hat}, |f̂(ξ)| = {mag}")
    elif choice == 3:
        values = dft.create_val()
        results = dft.dft(values)
        delta_x = float(input("What is the difference in x?"))
        frequencies = dft.find_frequencies(len(results), delta_x)
        print("Results:")
        for i in range(len(results)):
            print(results[i])
        print("\nFrequencies:")
        for i in range(len(frequencies)):
            print(frequencies[i])
    dest = bool(input("End? (blank for no)\n"))