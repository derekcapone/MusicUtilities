import numpy as np
import white_noise_generator as wn
import soundfile as sf


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


if __name__ == '__main__':
    sample_rate = 44100
    duration = 5  # 5 seconds
    iterations = 30


    song_arr = np.empty(shape=0, dtype=np.int16)
    for i in range(iterations):
        song_arr = np.concatenate([song_arr, wn.generate_white_noise(duration, sample_rate)])

    sf.write(r'../audio_files/test_files/test_file.wav', song_arr, sample_rate)
