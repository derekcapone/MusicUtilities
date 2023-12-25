# Idea is to generate a .wav file that consists of white noise with a "title_theme_pulse.wav" inserted in the middle
import numpy as np
import white_noise_generator as wn
import soundfile as sf

if __name__ == '__main__':
    sample_rate = 44100
    duration = 5  # 5 seconds
    iterations = 30


    song_arr = np.empty(shape=0, dtype=np.int16)
    for i in range(iterations):
        song_arr = np.concatenate([song_arr, wn.generate_white_noise(duration, sample_rate)])

    sf.write(r'audio_files/test_files/test_file.wav', song_arr, sample_rate)