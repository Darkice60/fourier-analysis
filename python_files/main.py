# Darkice60
# main file for fourier-analysis

import python_files.fourier_t as fourier_t            

choice = int(input("What would you like?\n1 - Fourier Transform at a frequency value?\n2 - Frequency finder using the Fourier Transform\n"))
dest = False

while not dest:
    func_string = input("Enter your function. \"USE CMATH FOR FUNCTIONS\"\n")
    func = fourier_t.create_func(func_string)
    if choice == 1:
        xi = float(input("xi value?\n"))
        t = float(input("integration domain? \"(make it so that the function decays to zero fast enough so that the domain to infinity is insignificant)\"\n"))
        n = float(input("number of steps?\n"))
        f_hat = fourier_t.fourier_transform(func, xi, t, n)
        mag = abs(f_hat)
        print(f"f̂(ξ) = {f_hat}, |f̂(ξ)| = {mag}")
    elif choice == 2:
        t = float(input("integration domain?\n"))
        n = float(input("number of steps?\n"))
        xi_min = float(input("what is the lowest frequency you would like to search for?\n"))
        xi_max = float(input("what is the highest frequency you would like to search for?\n"))
        peaks = fourier_t.find_high(func, t, n, xi_min, xi_max)
        refined = fourier_t.refine_peaks(func, t, n, peaks)
        for i in range(len(refined)):
            xi, f_hat, mag = refined[i]
            print(f"ξ = {xi}, f̂(ξ) = {f_hat}, |f̂(ξ)| = {mag}")
    dest = bool(input("End? (blank for no)\n"))