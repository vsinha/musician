import random
import time
from gtts import gTTS
import os
from noteslib import natural_notes

sleep_sec = 0.25
prev = None


def filename(note):
    return note + ".mp3"


def generate_file(note):
    obj = gTTS(note, lang="en", slow=False)
    obj.save(filename(note))


def pick_random(notes):
    global prev
    note = random.choice(notes)

    if prev is not None and prev == note:
        # Reduce the chance of repeats
        note = random.choice(notes)

    prev = note

    return note


def speak(note):
    print(note)

    file = filename(note)
    if not os.path.exists(file):
        generate_file(note)

    os.system("mpg321 --quiet " + file)


while True:
    note = pick_random(natural_notes)
    speak(note)
    time.sleep(sleep_sec)
