import numpy as np, pylab
from pydub import AudioSegment


speed = 100
nucleotids = ['A','C','G','T']
aminoacids = 'A R N D C Q E G H I L K M F P S T W Y V START STOP'.split(' ')

genome = list(open('genome.csv','r').read().replace('\n','').replace(' ',''))[:999]
aminos = open('amino.csv','r').read().split(',')[:-1][:333]

g_sound = [AudioSegment.from_file('./g_sounds/'+str(i+1)+'.wav',format='wav')[:speed] for i in range(4)]
a_sound = [AudioSegment.from_file('./a_sounds/'+str(i+1)+'.wav',format='wav')[:speed] for i in range(22)]

g_song = AudioSegment.silent(duration=speed)
a_song = AudioSegment.silent(duration=speed)

for g in genome:
    g_song += g_sound[nucleotids.index(g)]
    print g,

for a in aminos:
    a_song += a_sound[aminoacids.index(a)]
    a_song += a_sound[(aminoacids.index(a)-1) % 22]
    a_song += a_sound[(aminoacids.index(a)+1) % 22]
    print a,

g_song = g_song.apply_gain(+10.0)
song = a_song.overlay(g_song)

song.export('song.mp3',format='mp3')
