import note_value_enum
import note_finder


class Note:
    def __init__(self, note_string=None, frequency=None):
        """
        Constructor for Note, can only pass in one of note_string or frequency
        :param note_string: note_string used to instantiate the Note
        :param frequency: frequency used to instantiate the Note
        """
        if note_string is None and frequency is None:
            raise Exception("Either Note string or frequency is needed to instantiate Note object")

        if note_string is not None and frequency is not None:
            raise Exception("Can only instantiate Note if provided one parameter: Note string OR frequency")

        # Instantiate based on note string
        if note_string is not None:
            self.note_string = note_string
            self.note = note_value_enum.note_enum_factory(note_string)
            self.note_frequency = note_finder.find_note_frequency(note_string)

        # Instantiate based on frequency
        if frequency is not None:
            print("Using frequency to figure out note")
            self.note_frequency = frequency
            # TODO: Update finding closest note to have a maximum frequency difference
            self.note_string = min(note_finder.notes_frequencies, key=lambda note: abs(note_finder.notes_frequencies[note] - frequency))
            self.note = note_value_enum.note_enum_factory(self.note_string)


if __name__ == '__main__':
    n1 = Note(note_string="C#0/Db0")
    print(n1.note_frequency)
