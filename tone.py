import functools
import math
import operator
import numpy as np
import pyaudio
from notes import Note
from scales import scale
import chords
from scipy import interpolate
from operator import itemgetter


def sine(frequency, length, rate) -> np.ndarray:
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return np.sin(np.arange(length) * factor)


def shape(data, points, kind="slinear"):
    items = points.items()
    items = sorted(items, key=itemgetter(0))
    keys = list(map(itemgetter(0), items))
    vals = list(map(itemgetter(1), items))
    interp = interpolate.interp1d(keys, vals, kind=kind)
    factor = 1.0 / len(data)
    shape = interp(np.arange(len(data)) * factor)
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


def chord(notes, length):
    freqs = [sine(note.frequency(), length, 44100) for note in notes]
    return functools.reduce(operator.add, freqs) * 0.2
