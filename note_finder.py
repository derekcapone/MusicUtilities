import test_signal_generator
import frequency_analysis
import time

# Frequencies of all possible notes
notes_frequencies = {
    "C0": 16.35, "C#0/Db0": 17.32, "D0": 18.35, "D#0/Eb0": 19.45, "E0": 20.60,
    "F0": 21.83, "F#0/Gb0": 23.12, "G0": 24.50, "G#0/Ab0": 25.96, "A0": 27.50,
    "A#0/Bb0": 29.14, "B0": 30.87, "C1": 32.70, "C#1/Db1": 34.65, "D1": 36.71,
    "D#1/Eb1": 38.89, "E1": 41.20, "F1": 43.65, "F#1/Gb1": 46.25, "G1": 49.00,
    "G#1/Ab1": 51.91, "A1": 55.00, "A#1/Bb1": 58.27, "B1": 61.74, "C2": 65.41,
    "C#2/Db2": 69.30, "D2": 73.42, "D#2/Eb2": 77.78, "E2": 82.41, "F2": 87.31,
    "F#2/Gb2": 92.50, "G2": 98.00, "G#2/Ab2": 103.83, "A2": 110.00, "A#2/Bb2": 116.54,
    "B2": 123.47, "C3": 130.81, "C#3/Db3": 138.59, "D3": 146.83, "D#3/Eb3": 155.56, "E3": 164.81,
    "F3": 174.61, "F#3/Gb3": 185.00, "G3": 196.00, "G#3/Ab3": 207.65, "A3": 220.00,
    "A#3/Bb3": 233.08, "B3": 246.94,
    "C4": 261.63, "C#4/Db4": 277.18, "D4": 293.66, "D#4/Eb4": 311.13, "E4": 329.63,
    "F4": 349.23, "F#4/Gb4": 369.99, "G4": 392.00, "G#4/Ab4": 415.30, "A4": 440.00,
    "A#4/Bb4": 466.16, "B4": 493.88,
    "C5": 523.25, "C#5/Db5": 554.37, "D5": 587.33, "D#5/Eb5": 622.25, "E5": 659.25,
    "F5": 698.46, "F#5/Gb5": 739.99, "G5": 783.99, "G#5/Ab5": 830.61, "A5": 880.00,
    "A#5/Bb5": 932.33, "B5": 987.77,
    "C6": 1046.50, "C#6/Db6": 1108.73, "D6": 1174.66, "D#6/Eb6": 1244.51, "E6": 1318.51,
    "F6": 1396.91, "F#6/Gb6": 1479.98, "G6": 1567.98, "G#6/Ab6": 1661.22, "A6": 1760.00,
    "A#6/Bb6": 1864.66, "B6": 1975.53,
    "C7": 2093.00, "C#7/Db7": 2217.46, "D7": 2349.32, "D#7/Eb7": 2489.02, "E7": 2637.02,
    "F7": 2793.83, "F#7/Gb7": 2959.96, "G7": 3135.96, "G#7/Ab7": 3322.44, "A7": 3520.00,
    "A#7/Bb7": 3729.31, "B7": 3951.07,
    "C8": 4186.01, "C#8/Db8": 4434.92, "D8": 4698.63, "D#8/Eb8": 4978.03, "E8": 5274.04,
    "F8": 5587.65, "F#8/Gb8": 5919.91, "G8": 6271.93, "G#8/Ab8": 6644.88, "A8": 7040.00,
    "A#8/Bb8": 7458.62, "B8": 7902.13
}

# Enharmonic equivalent notes
enharmonic_equivalents = {
    # 0 notes
    "C#0": "Db0", "D#0": "Eb0", "F#0": "Gb0", "G#0": "Ab0", "A#0": "Bb0",
    "Db0": "C#0", "Eb0": "D#0", "Gb0": "D#0", "Ab0": "G#0", "Bb0": "A#0",
    # 1 notes
    "C#1": "Db1", "D#1": "Eb1", "F#1": "Gb1", "G#1": "Ab1", "A#1": "Bb1",
    "Db1": "C#1", "Eb1": "D#1", "Gb1": "D#1", "Ab1": "G#1", "Bb1": "A#1",
    # 2 notes
    "C#2": "Db2", "D#2": "Eb2", "F#2": "Gb2", "G#2": "Ab2", "A#2": "Bb2",
    "Db2": "C#2", "Eb2": "D#2", "Gb2": "D#2", "Ab2": "G#2", "Bb2": "A#2",
    # 3 notes
    "C#3": "Db3", "D#3": "Eb3", "F#3": "Gb3", "G#3": "Ab3", "A#3": "Bb3",
    "Db3": "C#3", "Eb3": "D#3", "Gb3": "D#3", "Ab3": "G#3", "Bb3": "A#3",
    # 4 notes
    "C#4": "Db4", "D#4": "Eb4", "F#4": "Gb4", "G#4": "Ab4", "A#4": "Bb4",
    "Db4": "C#4", "Eb4": "D#4", "Gb4": "F#4", "Ab4": "G#4", "Bb4": "A#4",
    # 5 notes
    "C#5": "Db5", "D#5": "Eb5", "F#5": "Gb5", "G#5": "Ab5", "A#5": "Bb5",
    "Db5": "C#5", "Eb5": "D#5", "Gb5": "F#5", "Ab5": "G#5", "Bb5": "A#5",
    # 6 notes
    "C#6": "Db6", "D#6": "Eb6", "F#6": "Gb6", "G#6": "Ab6", "A#6": "Bb6",
    "Db6": "C#6", "Eb6": "D#6", "Gb6": "F#6", "Ab6": "G#6", "Bb6": "A#6",
    # 7 notes
    "C#7": "Db7", "D#7": "Eb7", "F#7": "Gb7", "G#7": "Ab7", "A#7": "Bb7",
    "Db7": "C#7", "Eb7": "D#7", "Gb7": "F#7", "Ab7": "G#7", "Bb7": "A#7",
    # 8 notes
    "C#8": "Db8", "D#8": "Eb8", "F#8": "Gb8", "G#8": "Ab8", "A#8": "Bb8",
    "Db8": "C#8", "Eb8": "D#8", "Gb8": "F#8", "Ab8": "G#8", "Bb8": "A#8"
}


def generate_note_string(note_string):
    """
    Generates note string if passed in string has an enharmonic equivalent
    :param note_string: String of note (I.e. F#5, Ab8, G6, etc)
    :return: Enharmonic equivalent note string if existing, matching structure of enharmonic_equivalents map
    """
    # First try to use the initial string value
    enharmonic = enharmonic_equivalents.get(note_string)

    if not enharmonic:
        # If note does not exist in enharmonic equivalents, return original string
        return note_string

    # If enharmonic equivalent found, generate new string
    # Sharps are always first in "notes_frequencies" map
    return enharmonic + "/" + note_string if "#" in enharmonic else note_string + "/" + enharmonic


def find_note_frequency(note="A4"):
    """
    Finds frequency based on passed in note name
    :param note: String holding the name of the note to find frequency of
    :return: frequency of given note, -1 if note is invalid
    """
    # First check for valid string length
    if len(note) != 2 and len(note) != 3:
        return -1

    # First generate the necessary string
    note_string = generate_note_string(note)

    frequency = notes_frequencies.get(note_string)
    if frequency:
        print("Frequency of %s is %.02f Hz" % (note_string, frequency))
        return frequency
    else:
        print("Could not find frequency for %s" % note_string)
        return None


def find_single_note(frequency):
    """
    Finds the note that is closest in frequency to the given frequency
    :param frequency: frequency to test
    :return: closest note name, frequency diff between given note and closest note
    """
    # TODO: Update finding closest note to have a maximum frequency difference
    closest_note = min(notes_frequencies, key=lambda note: abs(notes_frequencies[note] - frequency))
    # Calculate the difference in frequency
    frequency_difference = abs(notes_frequencies[closest_note] - frequency)
    return closest_note, frequency_difference


def find_existing_notes(frequencies):
    existing_notes = []
    for frequency in frequencies:
        # TODO: Update finding closest note to have a maximum frequency difference
        existing_notes.append(min(notes_frequencies, key=lambda note: abs(notes_frequencies[note] - frequency)))
    return existing_notes


if __name__ == "__main__":
    sample_rate = 44100

    # Use test_signal_generator to generate signal
    t, tone_array = test_signal_generator.generate_int16_sine_wave(196, sampling_rate=sample_rate, duration=1)

    # Use frequency_analysis to extract the frequencies out of the signal
    fft_magnitude, fft_freq = frequency_analysis.generate_fft(tone_array, sample_rate)
    major_peaks_freq, _ = frequency_analysis.find_normalized_peaks(fft_magnitude, fft_freq)

    # Use note_finder to determine notes based on the extracted frequencies
    existing_notes = find_existing_notes(major_peaks_freq)
    print(existing_notes)
