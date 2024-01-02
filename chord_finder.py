from note import Note
from chord_interval import ChordInterval


def find_chord(notes):
    print(f"Finding chords for {notes}")


def find_chord_interval(root_note, next_note):
    """
    Takes 2 Note objects and finds the interval between them irrespective of octave
    :param root_note: Root note to use as base for interval calculation
    :param next_note: Note to find the interval from root note
    :return: Interval enum
    """
    print(f"Finding interval for {next_note} compared to {root_note}")
    if not isinstance(root_note, Note) or not isinstance(next_note, Note):
        raise Exception("root_note or next_note are not of type Note")

    # Determine the interval between the two notes
    interval = next_note.note - root_note.note
    if interval < 0:
        interval = 12 + interval  # 12 is total number of semi-tones


if __name__ == '__main__':
    note1 = Note("A4")
    note2 = Note("A#4")
    find_chord_interval(note1, note2)

    root_note = 11
    next_note = 6
    interval = next_note - root_note

    if interval < 0:
        interval = 12 + interval

    print(ChordInterval(interval))
