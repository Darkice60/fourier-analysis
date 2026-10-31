# fourier-analysis
A collection of Fourier analysis implementations and applications. These include numerical approximations of the Continuous Fourier Transform, Discrete Fourier Transform, and Fast Fourier Transform, as well as a simulated frequency-shift-keying (FSK) communication system.

# Features
The program has two main parts:

- The Fourier Transform implementations.
- The simulated communication system.

The Fourier Transform implementations include a numerical approximation of the Continuous Fourier Transform using Riemann sums, a manually implemented Discrete Fourier Transform, and a radix-2 Fast Fourier Transform utilizing the Cooley-Tukey algorithm.

The communication system utilizes frequency-shift keying (FSK) to encode binary data into discrete waveforms. Messages are converted into UTF-8 bytes, then binary data, with each bit represented by a different frequency. The receiver uses frequency analysis to reconstruct the original message from the transmitted waveform.

# Dependencies

- Python 3
- Numpy