import numpy as np


def generate_sine_wave(frequency, sampling_rate=44100, duration=1):
    """
    Generates a sine wave of the given characteristics in int16 format
    :param frequency: frequency of sine wave
    :param sampling_rate: sampling rate of sine wave
    :param duration: duration of signal
    :return: time array and int16 numpy array of generated sine wave
    """
    # Generate time values
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Generate sine wave values
    sine_wave = np.sin(2 * np.pi * frequency * t)

    # Scale to int16
    return t, np.array(sine_wave * 32767)
