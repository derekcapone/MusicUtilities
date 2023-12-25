import numpy as np
import soundfile as sf


def generate_white_noise(duration=5, sample_rate=44100):
    """
    Generate and return a numpy array of white noise of specified duration and sample rate
    :param duration: duration of white noise in seconds
    :param sample_rate: sample rate in Hz
    :return: np array of white noise normalized to 16-bits
    """
    # Generate white noise
    noise = np.random.normal(0, 1, duration * sample_rate)  # mean=0, std=1

    # Normalize to 16-bit range for WAV file
    return np.int16(noise / np.max(np.abs(noise)) * 32767)


def write_white_noise_to_file(file, normalized_wn_array, sample_rate=44100):
    sf.write(file, normalized_wn_array, sample_rate)


if __name__ == '__main__':
    white_noise_array = generate_white_noise()
    write_white_noise_to_file(r'audio_files/white_noise/test_file.wav', white_noise_array)
