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
        if len(chunk) < sample_per_bit:
            break
        chunk_dft = dft.dft(chunk)
        if abs(chunk_dft[4]) > abs(chunk_dft[8]) :
            bits.append(0)
        else:
            bits.append(1)
    return bits

def to_bytes(bits):
    if len(bits) % 8 != 0:
        raise ValueError("Bit count not divisible by 8!")
    bytes_val = []
    for i in range(0, len(bits) - 7, 8):
        byte = bits[i:i + 8]
        val = int("".join(map(str, byte)), 2)
        bytes_val.append(val)
    return bytes_val

def message_decode(bytes_val):
    return bytes(bytes_val).decode("utf-8")