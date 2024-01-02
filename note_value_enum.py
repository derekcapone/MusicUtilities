from enum import Enum


class NoteValue(Enum):
    C = 0
    C_sharp = 1
    D = 2
    D_sharp = 3
    E = 4
    F = 5
    F_sharp = 6
    G = 7
    G_sharp = 8
    A = 9
    A_sharp = 10
    B = 11


def note_enum_factory(note_str):
    """
    Use note string to find and generate simple note
    :return: NoteValue enum of passed in note
    """
    simple_note = parse_note_string(note_str)

    match simple_note:
        case "C":
            return NoteValue.C
        case "C#":
            return NoteValue.C_sharp
        case "D":
            return NoteValue.D
        case "D#":
            return NoteValue.D_sharp
        case "E":
            return NoteValue.E
        case "F":
            return NoteValue.F
        case "F#":
            return NoteValue.F_sharp
        case "G":
            return NoteValue.G
        case "G#":
            return NoteValue.G_sharp
        case "A":
            return NoteValue.A
        case "A#":
            return NoteValue.A_sharp
        case "B":
            return NoteValue.B
        case _:
            return f"Error finding simple note given {note_str}"


def parse_note_string(note_string):
    """
    Get the simple note string from the passed in note string
    :param note_string: string to determine the simple note string from
    :return: simple note string of passed in string
    """
    if len(note_string) < 2:
        return note_string[:1]

    # If note string has a sharp or a flat, parse both characters
    if note_string[1] == '#':
        return note_string[:2]
    # otherwise parse just the first
    else:
        return note_string[:1]


if __name__ == '__main__':
    note_string = "A#"
    note_enum_val = note_enum_factory(note_string)
    print(note_enum_val)
