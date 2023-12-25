from pydub import AudioSegment


def separate_audio_segments(file, chunk_length_ms=10000):
    # Load the WAV file
    audio = AudioSegment.from_file(file)

    # Calculate the number of chunks
    num_chunks = len(audio) // chunk_length_ms

    # Split the audio and save each chunk
    for i in range(num_chunks):
        start_ms = i * chunk_length_ms
        end_ms = start_ms + chunk_length_ms
        chunk = audio[start_ms:end_ms]
        chunk.export(f"audio_files/chunks/chunk{i}.wav", format="wav")


if __name__ == '__main__':
    file_name = r'audio_files/title_theme_full.mp3'
    separate_audio_segments(file_name)
