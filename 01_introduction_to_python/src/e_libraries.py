from scamp import *

MODE_DICT = {
    'minor': ['W', 'H', 'W', 'W', 'H', 'W', 'W'],
    'major': ['W', 'W', 'H', 'W', 'W', 'W', 'H']
}

MIDDLE_NOTES = {
    'a': 57,
    'a_sharp': 58,
    'b': 59,
    'c': 60,
    'c_sharp': 61,
    'd': 62,
    'd_sharp': 63,
    'e': 64,
    'f': 65,
    'f_sharp': 66,
    'g': 67,
    'g_sharp': 68
}

middle_c_midi = 60

def generate_scale(note: str = "c", mode: str = 'major') -> list:
    """
        This function generates a scale based on the note and mode.
        takes a note and also a mode.
    """
    scale = []

    stepper = MIDDLE_NOTES[note]

    for step in MODE_DICT[mode]:
        if step == "W":
            scale.append(stepper)
            stepper = stepper + 2
        else:
            scale.append(stepper)
            stepper = stepper + 1
    
    return scale

s = Session()

piano = s.new_part('piano')

c_major = generate_scale()

for note in c_major:
    piano.play_note(note, 1, 1)