import logging
import operator

from .harmony import Harmony


logger = logging.getLogger(__name__)


class Song(object):
    """ Container for a Song object. """

    def __init__(self, song=None, root_key=None, bpm=None):
        self.song = song
        self.root_key = root_key
        self.root_value = Harmony.HARMONY[self.root_key]
        self.bpm = bpm

    def __repr__(self):
        return '<Song song="{0.song!r}" key="{0.root_key}" root_value="{0.root_value}">'.format(self)


def evaluate_harmony(songs=None, root_key=None):
    """
    :param songs: A list of Song objects
    :param root_key: A string representing the root_key or seed_key for our set list.
    :return: A list of Song objects ordered by key progression.
    :return: A list of Song objects that we were unable to place.
    :rtype: list (of Song objects)
    """

    # sort our list of Songs by root_key_value
    songs = sorted(songs, key=operator.attrgetter('root_value'))
    harm = Harmony(root_key)
    set_list = []
    x = 0
    len_songs = len(songs)

    # attempt at most 2 passes at placing the songs into an 
    # ordered set_list.
    while x < len_songs and len(songs) > 0:
        for i, song in enumerate(songs):
            logger.debug('{song}->{key}'.format(song=song.song, key=song.root_key))
            if song.root_key in harm.harmonies:
                set_list.append(songs.pop(i))
                harm = Harmony(song.root_key)
                logger.debug('harm.harmonies.values->{values}'.format(values=harm.harmonies))
        x += 1

    return set_list, songs
