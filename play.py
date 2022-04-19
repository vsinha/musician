import time
import pyaudio
import numpy as np
import notes
from pick_random import pick_random
import scales
import tone

volume = 0.5  # range [0.0, 1.0]
duration = 0.5  # in seconds, may be float


if __name__ == "__main__":

    scale = scales.scale(notes.Note("A3"), "pentatonic")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

    while True:
        note = pick_random(scale, never_repeats=True)
        samples = tone.pluck1(note, length=duration) * volume
        stream.write(samples.astype(np.float32).tobytes())
        time.sleep(0.25)

    stream.stop_stream()
    stream.close()
    p.terminate()
