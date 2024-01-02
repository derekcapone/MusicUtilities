import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from signal_generation import test_signal_generator


def generate_fft(signal, sample_rate):
    """
    Generates an FFT based on the given signal and sample rate
    :param signal: Signal to perform FFT on
    :param sample_rate: Sample rate of the signal
    :return: Array holding FFT Magnitude, Array holding FFT frequency
    """
    # Perform FFT
    fft_result = np.fft.fft(signal)
    fft_magnitude = np.abs(fft_result)

    # Frequency bins
    fft_freq = np.fft.fftfreq(len(fft_magnitude), 1 / sample_rate)
    return fft_magnitude, fft_freq


def find_normalized_peaks(fft_magnitude, fft_freq, height=0.5):
    """
    Normalizes the magnitude of the FFT and finds the peaks based on the given height
    :param fft_magnitude: Numpy array containing the calculated FFT
    :param fft_freq: Numpy array containing the frequency of the FFT
    :param height: Minimum height of the FFT normalized to 1 that will be a peak. 0.5 height will be a height limit of 50% of the maximum height
    :return: Returns an array of the peaks and frequency of peaks that surpass the minimum height in the provided fft_magnitude
    """
    # Normalize the magnitude
    normalized_magnitude = fft_magnitude / np.max(fft_magnitude)

    # Find Peaks
    peaks, _ = find_peaks(normalized_magnitude, height=height)

    # Filter out negative frequencies
    positive_frequencies = fft_freq > 0
    peaks = peaks[positive_frequencies[peaks]]

    # Sort peaks by magnitude
    sorted_peaks = peaks[np.argsort(fft_magnitude[peaks])][::-1]

    # Major Peaks
    major_peaks_freq = fft_freq[sorted_peaks]
    major_peaks_magnitude = fft_magnitude[sorted_peaks]
    return major_peaks_freq, major_peaks_magnitude


if __name__ == "__main__":
    # Parameters
    frequency = 440  # frequency of the sine wave (Hz)
    sampling_rate = 44100  # sampling rate (samples per second)
    duration = 1  # duration of the signal (seconds)

    # Generate sine wave
    t, tone_array = test_signal_generator.generate_sine_wave(196, sampling_rate=sampling_rate, duration=1)
    t2, tone_array2 = test_signal_generator.generate_sine_wave(440, sampling_rate=sampling_rate, duration=1)

    overall_signal = tone_array + tone_array2

    # Find FFT and find peaks
    fft_magnitude, fft_freq = generate_fft(overall_signal, sampling_rate)
    major_peaks_freq, major_peaks_magnitude = find_normalized_peaks(fft_magnitude, fft_freq)

    # Plotting (Optional)
    plt.plot(fft_freq, fft_magnitude)
    plt.scatter(major_peaks_freq, major_peaks_magnitude, color='red')  # Mark the peaks
    plt.title("FFT of the Sine Wave with Peaks")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, 600)
    plt.show()
