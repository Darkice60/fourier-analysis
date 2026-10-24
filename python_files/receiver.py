# Darkice60
# reciever file for fourier-analysis

# import the FFT for decoding
import fast_ft as fft

# this "reads" the signal from the file
def read_file(file_name):
    # create list of all signal values
    signal = []
    # open the file
    with open(file_name, "r") as f:
        # append all the lines to teh signal list
        for line in f:
            signal.append(float(line.strip()))
    # return the signal
    return signal

# convert the signal to bits
def to_bits(signal, time_bit, sample_rate):
    # create a list of bits
    bits = []
    # calc the amt of smaples per bit
    sample_per_bit = int(time_bit * sample_rate)
    # for how long the signal is with increments of the amt of smaples bper bit
    for i in range(0, len(signal), sample_per_bit):
        # get the chunk that contains a bit
        chunk = signal[i:i + sample_per_bit]
        # if the chunk is corrputed/cutoff, break out of the loop
        if len(chunk) < sample_per_bit:
            break
        # FFT the chunk
        chunk_fft = fft.fft(chunk)
        # if the magnitude of frequecy 40 is higher than eight
        if abs(chunk_fft[4]) > abs(chunk_fft[8]) :
            # appenend a 0 as the bit
            bits.append(0)
        else:
            # otherwise append 1
            bits.append(1)
    # return the list of bits
    return bits

# convert bits to bytes
def to_bytes(bits):
    # if the length of bits is not divisble by 8, raise a ValueError
    if len(bits) % 8 != 0:
        raise ValueError("Bit count not divisible by 8!")
    # create a list for the bytes
    bytes_val = []
    # for the each byte chunk in bits
    for i in range(0, len(bits) - 7, 8):
        # create a list of 8 bits to represent a byte
        byte = bits[i:i + 8]
        # create the byte
        val = int("".join(map(str, byte)), 2)
        # add the byte to the list
        bytes_val.append(val)
    # return the bytes list
    return bytes_val

# decode the bytes msg
def message_decode(bytes_val):
    # return the decoded bytes msg
    return bytes(bytes_val).decode("utf-8")