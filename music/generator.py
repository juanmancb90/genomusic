import random

from musical import Note, Scale
from musical import save

from .timeline import Hit, Timeline


def sampler(data, name):
    genome = [x.replace('\n', '').replace(' ', '') for x in data]
    numbers = []

    for g in genome:
        if g == 'A':
            numbers.append(-2)

        if g == 'C':
            numbers.append(-1)

        if g == 'G':
            numbers.append(1)

        if g == 'T':
            numbers.append(2)

      # Define key and scale
    key = Note('C4')
    scale = Scale(key, 'phrygian')
    time = 0.0  # Keep track of currect note placement time in seconds
    ardu_time = [str(time*1000)]

    timeline = Timeline()
    note = key

      # Semi-randomly queue notes from the scale
    for i in range(len(genome)):
        if note.index > 50 or note.index < 24:
           # If note goes out of comfort zone, randomly place back at base octave
            note = scale.get((numbers[i]+2) * 2)
            note = note.at_octave(key.octave)
        else:
          # Transpose the note by some small random interval
            note = scale.transpose(note, numbers[i])

        length = random.choice((0.125, 0.125, 0.25))
        timeline.add(time, Hit(note, length + 0.125))
        time += length
        ardu_time.append(str(time*1000))

        # Resolve
        note = scale.transpose(key, random.choice((-1, 1, 4)))
        timeline.add(time, Hit(note, 0.75))  # Tension
        timeline.add(time + 0.5, Hit(key, 4.0))  # Resolution

        print("Rendering audio...")

        data = timeline.render()

        print("Applying Chorus effect...")

        data = data * 0.5

        print("Exporting audio...")

        save.save_wave(data, 'media/music/{0}.mp3'.format(name), rate=44100)
        open('media/txt/{0}.txt'.format(name), 'w').write('\n'.join(ardu_time))
        return ('media/music/{0}.mp3'.format(name), 'media/txt/{0}.txt'.format(name))
