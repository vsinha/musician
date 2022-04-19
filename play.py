import time
import pyaudio
import numpy as np
import notes
from pick_random import pick_random
import scales

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 3.0  # in seconds, may be float


def play_note(note, stream):
    f = notes.frequencies[note] / 2

    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)


if __name__ == "__main__":

    scale = scales.scale(notes.Note("A"), "pentatonic")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    while True:
        note = pick_random.pick_random(scale, never_repeats=True)
        play_note(note, stream)
        time.sleep(0.5)

    stream.stop_stream()
    stream.close()
    p.terminate()
