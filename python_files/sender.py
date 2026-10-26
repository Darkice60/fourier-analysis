# Darkice60
# sender file for fourier-analysis

#importy math
import math as m

# convert the data to bytes
def get_bytes(msg):
    # get the msg as bytes
    data = " ".join(format(b, "08b") for b in msg)
    # put the bytes in a list
    data_lst = data.split(" ")
    # return the list
    return data_lst

# convert bytes to bits
def get_bits(data):
    # create a list for bits
    bits = []
    # create a for loop for the bytes
    for byte in data:
        # add the bits into byte
        bits.append(list(byte))
    return bits

# create the wave using an inverse transform
def form_wave(bits, time_bit, sample_rate):
    # craete a list for the "signal"
    signal = []
    # the amt of samples per bit is the time per bit * the amout of samples per second
    samples = int(time_bit * sample_rate)
    # for loop to search through the bytes
    for bytes in bits:
        # for loop for the bits in bytes
        for bit in bytes:
            # if the bit is 0 frequcney is 40 Hz, if 1 is 80 Hz
            frequency = 40 if bit == "0" else 80
            # for the amount of smaples per bit
            for n in range(samples):
                # write the signal and add it to the signal lits
                t = n / sample_rate
                signal.append(m.sin(2 * m.pi * frequency * t))
    # return the signal lits
    return signal

# write teh signal list to a file
def write_file(file_name, signal):
    # open the file to write
    with open(file_name, "w") as f:
        # for loop of each smaple in signal
        for sample in signal:
            # write each sample into the file
            f.write(f"{sample}\n")