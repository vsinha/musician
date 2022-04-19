import random

previous_pick = None


def pick_random(items, never_repeats=False):
    global previous_pick
    item = random.choice(items)
    if never_repeats:
        while item == previous_pick:
            item = random.choice(items)
    else:
        if previous_pick == item:
            # Reduce the chance of repeats
            item = random.choice(items)

    previous_pick = item
    return item
