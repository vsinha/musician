import random
import time
import pyaudio
import numpy as np

natural_notes: list[str] = ["A", "B", "C", "D", "E", "F", "G"]
all_notes = [
    "A",
    "A#",
    "B",
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
]


scales = {
    "major": "WWHWWWH",
    "pentatonic": "TWWTW",
    "minor": "WHWWHWW",
    "harmonic_minor": "WHWWHTH",
    "dorian": "WHWWWHW",
    "mixolydian": "WWHWWHW",
}

note_frequencies = {
    "A": 440.0,
    "A#": 466.16,
    "B": 493.88,
    "C": 523.25,
    "C#": 554.37,
    "D": 587.33,
    "D#": 622.25,
    "E": 659.25,
    "F": 698.46,
    "F#": 739.99,
    "G": 783.99,
    "G#": 830.61,
}


def get_scale(key, which_scale):
    steps = scales[which_scale]
    increments = []

    for char in steps:
        if char == "W":
            increments.append(2)
        elif char == "T":
            increments.append(3)
        elif char == "H":
            increments.append(1)
        else:
            print("Something's wrong, got a ", char)

    # find our starting index
    idx = all_notes.index(key)

    notes = [key]
    for increment in increments:
        idx = (idx + increment) % len(all_notes)
        note = all_notes[idx]
        notes.append(note)

    # we want our scale to not re-include the note we started with
    notes = notes[:-1]

    print("key:", key, which_scale, ", notes:", notes)
    return notes


prev = None


def choose(notes):
    global prev
    note = random.choice(notes)
    while note == prev:
        note = random.choice(notes)
    prev = note
    print(note)
    return note


# Set up pyaudio
p = pyaudio.PyAudio()
volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 3.0  # in seconds, may be float
# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)


def play_note(note):
    f = note_frequencies[note] / 2

    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)


scale = get_scale("A", "pentatonic")

while True:
    note = choose(scale)
    play_note(note)
    time.sleep(0.5)

stream.stop_stream()
stream.close()
p.terminate()
