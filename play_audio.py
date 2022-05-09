import random
import numpy as np
import pyaudio
from notes import Note
from scales import scale
import chords
from tone import chord, pluck1


class Audio:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paFloat32, channels=1, rate=44100, output=True
        )
        self.chunks = []

    def play(self):
        chunk = np.concatenate(self.chunks) * 0.25
        self.stream.write(chunk.astype(np.float32).tobytes())

    def queue(self, note_chunks):
        for chunk in note_chunks:
            self.chunks.append(chunk)

    def stop(self):
        self.stream.stop_stream()


def play_scale_chords():
    root = Note("A", 3)
    notes = scale(root, "major")

    chunks = []

    for note in notes:
        c = chord(chords.chord(note, "major"), length=0.5)
        chunks.append(c)

    chunk = np.concatenate(chunks) * 0.25
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
    stream.write(chunk.astype(np.float32).tobytes())
    stream.close()
    p.terminate()


def play_notes(notes):
    chunks = []

    for note in notes:
        c = pluck1(note, length=0.25)
        chunks.append(c)

    chunk = np.concatenate(chunks) * 0.25
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
    stream.write(chunk.astype(np.float32).tobytes())
    stream.close()
    p.terminate()


def play_scale_unbatched():
    root = Note("A", 3)
    notes = scale(root, "major")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

    for note in notes:
        chunk = pluck1(note, length=0.25)
        stream.write(chunk.astype(np.float32).tobytes())

    stream.close()
    p.terminate()


audio = Audio()
notes = []
root = Note("A", octave=3)
scale_notes = scale(root, "pentatonic")
for bar in range(0, 16):
    if bar % 2 == 0:
        bar_notes = [
            (root, 0.5),
            (random.choice(scale_notes), 0.25),
            (random.choice(scale_notes), 0.25),
        ]
    else:
        bar_notes = [
            (random.choice(scale_notes), 0.25),
            (random.choice(scale_notes), 0.25),
            (random.choice(scale_notes), 0.25),
            (random.choice(scale_notes), 0.25),
        ]

    print(bar_notes)
    for note, time in bar_notes:
        notes.append(pluck1(note, time))
    notes.append(pluck1(root, 0.5))

audio.queue(notes)
audio.play()
