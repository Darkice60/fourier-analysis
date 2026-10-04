# Darkice60
# sender file for fourier-analysis

def get_bytes(msg):
    data = " ".join(format(b, "08b") for b in msg)
    data_lst = data.split( )
    return data_lst