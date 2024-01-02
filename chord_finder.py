from note import Note
from interval import Interval


def find_chord(notes):
    print(f"Finding chords for {notes}")


def find_simple_interval(root_note, next_note):
    """
    Takes 2 Note objects and finds the interval between them irrespective of octave
    :param root_note: Root note to use as base for interval calculation
    :param next_note: Note to find the interval from root note
    :return: Interval enum
    """
    print(f"Finding interval for {next_note} compared to {root_note}")
    if not isinstance(root_note, Note) or not isinstance(next_note, Note):
        raise Exception("root_note or next_note are not of type Note")


if __name__ == '__main__':
    note1 = Note("A4")
    print(note1.note_string)
    note2 = Note("A#4/Bb4")
    print(note2.note_string)
