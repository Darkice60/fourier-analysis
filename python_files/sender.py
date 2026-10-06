# Darkice60
# sender file for fourier-analysis

import math as m

def get_bytes(msg):
    data = " ".join(format(b, "08b") for b in msg)
    data_lst = data.split(" ")
    return data_lst

def get_bits(data):
    bits = []
    for byte in data:
        bits.append(list(byte))
    return bits

def form_wave(bits):
    signal = []
    time_bit = 0.1
    sample_rate = 1000
    samples = int(time_bit * sample_rate)
    for bytes in bits:
        for bit in bytes:
            frequency = 40 if bit == "0" else 80
            for n in range(samples):
                t = n / sample_rate
                signal.append(m.sin(2 * m.pi * frequency * t))
    return signal

def write_file(file_name, signal):
    with open(file_name, "w") as f:
        for sample in signal:
            f.write(f"{sample}\n")