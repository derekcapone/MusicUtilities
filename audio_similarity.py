import librosa
import numpy as np
from scipy.spatial.distance import euclidean


# Function to load and extract MFCCs from an audio file
def extract_mfcc(file_path, n_mfcc=13):
    # Load the audio file
    audio, sample_rate = librosa.load(file_path, sr=None)
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=n_mfcc)
    # Average the MFCCs across time
    mfccs_mean = np.mean(mfccs, axis=1)
    return mfccs_mean


def find_euclidian_distance(file1, file2):
    # Extract MFCCs from both audio files
    mfccs_1 = extract_mfcc(file_path_1)
    mfccs_2 = extract_mfcc(file_path_2)

    # Calculate Euclidean distance between the two sets of MFCCs
    return euclidean(mfccs_1, mfccs_2)


if __name__ == "__main__":
    # Placeholder paths for two audio files
    file_path_1 = r'audio_files/title_theme_pulse.wav'
    file_path_2 = r'audio_files/random_song.wav'

    distance = find_euclidian_distance(file_path_1, file_path_2)
    print(distance)
