import csv

from harmonic_shuffle.core import Song, evaluate_harmony


sng = []

sng.append(Song(song='Cajmere - Brighter Days (Gene Ferris)', root_key='G'))
sng.append(Song(song='KC Flightt - Voices 2000', root_key='Em'))
sng.append(Song(song='Raze - BREAK 4 LOVE (Funk Rockers Remix)', root_key='Cm'))
sng.append(Song(song='M1 - BLUNTED AGAIN (Original Mix)', root_key='Ab'))
sng.append(Song(song='Frankie Knuckles - THE WHISTLE SONGSupernova Remix', root_key='Em'))
sng.append(Song(song='Chez Damier - CAN YOU FEEL ITSupernova Remix', root_key='B'))
sng.append(Song(song='Soul Central- STRINGS OF LIFESupernova Remix', root_key='F#'))
sng.append(Song(song='Hot Since 82 - SOMEBODY EVERYBODY', root_key='Ab'))
sng.append(Song(song='Inner City - GOOD LIFEMatt Smallwood Remix', root_key='Bm'))
sng.append(Song(song='Inner City - BIG FUN 2013', root_key='Ebm'))
sng.append(Song(song='Frankie Knuckles - Your Love', root_key='Em'))
sng.append(Song(song='Aly-Us - Follow Me (Oliver Desment)', root_key='Cm'))

def read_directory(filename):

    songs = []
    audio = beats.open(filename)

def read_csv(filename):
    songs = []

    with open(filename, 'rb') as csvfile:
        songreader = csv.reader(csvfile)
        for row in songreader:
            songs.append(Song(song=row['song'], root_key=row['root_key']))

    return songs


for i,s in enumerate(sng):
  sngs = sng[:]
  del sngs[i]
  used, unused = evaluate_harmony(songs=sngs, root_key=s.root_key) 
  print 'Seed : {song} -> {lused}:{unused}\n\tused->{used}\n\n'.format(song=s.song,used=used, unused=len(unused), lused=len(used))
