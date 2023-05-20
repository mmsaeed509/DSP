#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

# Import the necessary libraries/modules #
from scipy.fft import fft, ifft
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import COLORS


## ------- Problem No. 1 ------- ##


# Read the WAV file #
print(COLORS.BOLD_PURPLE + "\n[*] Reading the WAV File Record... " + COLORS.RESET_COLOR)
sr, sig = wavfile.read("wav/FFT_SampleRateRecord.wav")

# Convert the signal to a NumPy array #
print(COLORS.BOLD_PURPLE + "\n[+] Converting the signal to a NumPy array... " + COLORS.RESET_COLOR)
x = np.asarray(sig)

# Apply the FFT to the signal #
print(COLORS.BOLD_PURPLE + "\n[+] Applying the FFT to the signal... " + COLORS.RESET_COLOR)
y = fft(x)

# Perform inverse FFT to obtain the reconstructed signal #
print(COLORS.BOLD_PURPLE + "\n[+] Performing inverse FFT to obtain the reconstructed signal... " + COLORS.RESET_COLOR)
yinv = ifft(y)

# Calculate the magnitude spectrum of the original signal #
print(COLORS.BOLD_PURPLE + "\n[+] Calculating the magnitude spectrum of the original signal... " + COLORS.RESET_COLOR)
magnitude_spectrum_signal = np.abs(y)

# Plot the magnitude spectrum of the original signal #
print(COLORS.BOLD_PURPLE + "\n[+] Plotting the magnitude spectrum of the original signal... " + COLORS.RESET_COLOR)
plt.plot(magnitude_spectrum_signal)
plt.show()

# Calculate the magnitude spectrum of the FFT #
print(COLORS.BOLD_PURPLE + "\n[+] Calculating the magnitude spectrum of the FFT... " + COLORS.RESET_COLOR)
magnitude_spectrum = np.abs(y)

# Plot the magnitude spectrum of the FFT #
print(COLORS.BOLD_PURPLE + "\n[+] Plotting the magnitude spectrum of the FFT... " + COLORS.RESET_COLOR)
plt.plot(magnitude_spectrum)
plt.show()

# Calculate the magnitude spectrum of the inverse FFT #
print(COLORS.BOLD_PURPLE + "\n[+] Calculating the magnitude spectrum of the inverse FFT... " + COLORS.RESET_COLOR)
magnitude_spectrum_in = np.abs(yinv)

# Plot the magnitude spectrum of the inverse FFT #
print(COLORS.BOLD_PURPLE + "\n[+] Plotting the magnitude spectrum of the inverse FFT... " + COLORS.RESET_COLOR)
plt.plot(magnitude_spectrum_in)
plt.show()

# Convert the inverse FFT output to 16-bit integer values #
print(COLORS.BOLD_PURPLE + "\n[+] Converting the inverse FFT output to 16-bit integer values... " + COLORS.RESET_COLOR)
ifft_output = np.int16(yinv.real)

# Write the reconstructed signal to a WAV file #
print(COLORS.BOLD_PURPLE + "\n[+] Writing the reconstructed signal to a WAV file... " + COLORS.RESET_COLOR)
write("wav/ReverseRecord.wav", sr, ifft_output)


## ------- Problem No. 2 ------- ##


# Define a function for convolution #
def convolution(x, h):
    # Perform convolution using np.convolve #
    print(COLORS.BOLD_PURPLE + "\n[+] Performing convolution using" +
          COLORS.BOLD_RED + " `np.convolve`" + COLORS.RESET_COLOR)
    y = np.convolve(x, h)
    return y


# Generate the impulse response function #
def generate_impulse_response():
    # Create an array for the impulse response #
    h = np.zeros(99)
    for i in range(99):
        if i != 49:
            # Calculate the sinc function for non-zero indices #
            h[i] = 0.31752 * np.sin(0.314159 * (i - 49.00001)) / (i - 49.00001)
        else:
            # Set the value at index 49 to a constant value (avoiding division by zero) #
            h[i] = 0.31752
        # Apply a Hamming window to the impulse response #
        h[i] = h[i] * (0.54 - 0.46 * np.cos(0.0641114 * i))
    return h


# Generate the impulse response #
print(COLORS.BOLD_PURPLE + "\n[+] Generate the Impulse Response... " + COLORS.RESET_COLOR)
h = generate_impulse_response()

# Plot the impulse response #
print(COLORS.BOLD_PURPLE + "\n[+] Plotting the Impulse Response... " + COLORS.RESET_COLOR)
n = np.arange(99)
plt.plot(n, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('Impulse Response')
plt.grid(True)
plt.show()

# Create an input signal (unit impulse) #
print(COLORS.BOLD_PURPLE + "\n[+] Creating an input signal (unit impulse)... " + COLORS.RESET_COLOR)
x = np.zeros(500)
x[0] = 1

# Perform convolution of the input signal and impulse response #
print(COLORS.BOLD_PURPLE + "\n[+] Performing convolution of the input signal and Impulse Response... "
      + COLORS.RESET_COLOR)
y = convolution(x, h)

# Print the output of the convolution #
print(COLORS.BOLD_CYAN)
print(y)
print(COLORS.RESET_COLOR)

# Plot the output signal #
print(COLORS.BOLD_PURPLE + "[+] Plotting the output signal... " + COLORS.RESET_COLOR)
plt.plot(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolution Output')
plt.grid(True)
plt.show()

# DONE! #
print(COLORS.BOLD_GREEN + "\n[✔] D O N E !" + COLORS.RESET_COLOR)
