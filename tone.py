import math
import numpy
import pyaudio
from notes import Note
import scales
from scipy import interpolate
from operator import itemgetter


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def shape(data, points, kind="slinear"):
    items = points.items()
    items = sorted(items, key=itemgetter(0))
    keys = list(map(itemgetter(0), items))
    vals = list(map(itemgetter(1), items))
    interp = interpolate.interp1d(keys, vals, kind=kind)
    factor = 1.0 / len(data)
    shape = interp(numpy.arange(len(data)) * factor)
    return data * shape


def harmonics1(freq, length):
    a = sine(freq * 1.00, length, 44100)
    b = sine(freq * 2.00, length, 44100) * 0.5
    c = sine(freq * 4.00, length, 44100) * 0.125
    return (a + b + c) * 0.2


def harmonics2(freq, length):
    a = sine(freq * 1.00, length, 44100)
    b = sine(freq * 2.00, length, 44100) * 0.5
    return (a + b) * 0.2


def pluck1(note, length=1.0):
    chunk = harmonics1(note.frequency(), length)
    return shape(chunk, {0.0: 0.0, 0.005: 1.0, 0.25: 0.5, 0.9: 0.1, 1.0: 0.0})


def pluck2(note, length=1.0):
    chunk = harmonics2(note.frequency(), length)
    return shape(chunk, {0.0: 0.0, 0.5: 0.75, 0.8: 0.4, 1.0: 0.1})


def play_scale_batch():
    root = Note("A", 3)
    scale = scales.scale(root, "major")

    chunks = []

    for note in scale:
        chunks.append(pluck1(note, length=0.25))

    chunk = numpy.concatenate(chunks) * 0.25
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
    stream.write(chunk.astype(numpy.float32).tobytes())
    stream.close()
    p.terminate()


def play_scale_unbatched():
    root = Note("A", 3)
    scale = scales.scale(root, "major")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

    for note in scale:
        chunk = pluck1(note, length=0.25)
        stream.write(chunk.astype(numpy.float32).tobytes())

    stream.close()
    p.terminate()
