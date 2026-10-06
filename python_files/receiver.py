def read_file(file_name):
    signal = []
    with open(file_name, "r") as f:
        for line in f:
            signal.append(line.strip())
    return signal

# def to_bits(signal, time_bit, sample_rate):
#     bits = []
#     sample_per_bit = int(time_bit * sample_rate)
#         for 
#     return bits