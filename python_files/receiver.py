# Darkice60
# reciever file for fourier-analysis

import discrete_ft as dft

def read_file(file_name):
    signal = []
    with open(file_name, "r") as f:
        for line in f:
            signal.append(float(line.strip()))
    return signal

def to_bits(signal, time_bit, sample_rate):
    bits = []
    sample_per_bit = int(time_bit * sample_rate)
    for i in range(0, len(signal), sample_per_bit):
        chunk = signal[i:i + sample_per_bit]
        chunk_dft = dft.dft(chunk)
        if chunk_dft[4] > chunk_dft[8]:
            bits.append(0)
        else:
            bits.append(1)
    return bits