import random

from musical.theory import Note, Scale
from musical.audio import save

from timeline import Hit, Timeline

genome = list(open('genome.csv', 'r').read().replace('\n', '').replace(' ', ''))
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
time = 0.0 # Keep track of currect note placement time in seconds
ardu_time = []

timeline = Timeline()

note = key

# Semi-randomly queue notes from the scale
for i in xrange(len(genome)):
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
  ardu_time.append(str(length*1000))

# Resolve
note = scale.transpose(key, random.choice((-1, 1, 4)))
timeline.add(time, Hit(note, 0.75))     # Tension
timeline.add(time + 0.5, Hit(key, 4.0)) # Resolution

print("Rendering audio...")

data = timeline.render()

print("Applying Chorus effect...")

#data = effect.chorus(data, freq=3.14159)
# Reduce volume to 50%
data = data * 0.5

print("Exporting audio...")

save.save_wave(data, 'music.mp3', rate=44100)
open('timeduino.txt','w').write('\n'.join(ardu_time))
print("Done!")
