import note_enum


class Note:
    def __init__(self, note_string):
        print(f"Creating note class for {note_string}")
        self.note_string = note_string
        self.note = note_enum.note_enum_factory(note_string)

if __name__ == '__main__':
    n1 = Note()
    print(n1)