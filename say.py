import time
from gtts import gTTS
import os
import noteslib
from pick_random import pick_random

sleep_sec = 0.25

cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes-cache")


def filename(note):
    return os.path.join(cache_dir, "spoken-" + note + ".mp3")


def generate_file(note):
    obj = gTTS(note, lang="en", slow=False)
    obj.save(filename(note))


def speak(note):
    file = filename(note)
    if not os.path.exists(file):
        generate_file(note)

    os.system("mpg321 --quiet " + file)


if __name__ == "__main__":
    os.mkdir(cache_dir)

    while True:
        note = pick_random(noteslib.natural_note_names)
        speak(note)
        time.sleep(sleep_sec)
