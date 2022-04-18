import random
import time
import pyaudio
import numpy as np
import noteslib
import scales


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
    f = noteslib.frequencies[note] / 2

    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)


scale = scales.get_scale("A", "pentatonic")

while True:
    note = choose(scale)
    play_note(note)
    time.sleep(0.5)

stream.stop_stream()
stream.close()
p.terminate()
