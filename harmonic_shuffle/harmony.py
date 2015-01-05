import logging

logger = logging.getLogger(__name__)


class Harmony(object):
    # numeric representation of the Circle of 5ths.
    HARMONY = {
        'G': 1,
        'D': 2,
        'A': 3,
        'E': 4,
        'B': 5,
        'F#': 6,
        'Gb': 6,
        'Db': 7,
        'C#': 7,
        'Ab': 8,
        'Eb': 9,
        'Bb': 10,
        'F': 11,
        'C': 12,
        'Em': 101,
        'Bm': 102,
        'F#m': 103,
        'Gbm': 103,
        'Dbm': 104,
        'C#m': 104,
        'G#m': 105,
        'Ebm': 106,
        'D#m': 106,
        'A#m': 107,
        'Bbm': 107,
        'Fm': 108,
        'Cm': 109,
        'Gm': 110,
        'Dm': 111,
        'Am': 112,
    }

    def __init__(self, root_key):
        """
        :param root_key: A string value representing the root key signature for the song.
        """

        if root_key not in Harmony.HARMONY.keys():
            raise LookupError('{key} is not reconized'.format(key=root_key))

        self.root_key = root_key
        self.root_key_value = Harmony.HARMONY[self.root_key]
        # a list representing all compatible tone for a given root_key
        self.harmonies = self._get_value(self.root_key_value) + self.down_shift() + self.up_shift() + self.minor()

    def __repr__(self):
        return '<Harmony key={0.root_key} value={0.root_key_value}>'.format(self)

    @staticmethod
    def _get_value(value):
        """ performs a look-up of the HARMONY dictionary by value.
        :parameter value: An integer representing a harmonic key
        :return: A list of keys
        :rtype list:
        """

        return [note for note, fifth_value in Harmony.HARMONY.iteritems() if value == fifth_value]

    def down_shift(self):
        """ Fetches the next key(s) that represents a single tone downward
        :return: A list representing a compatible key
        :rtype list:
        """

        down = []

        # handle a roll over at position "1" on the wheel. in the case of 1 or 101 we down
        # shift to 12 or 112
        if self.root_key_value == 1:
            down = Harmony._get_value(12)
        elif self.root_key_value == 101:
            down = Harmony._get_value(112)
        else:
            down = Harmony._get_value(self.root_key_value - 1)

        return down

    def up_shift(self):
        """ Fetches the next key(s) that represents a single tone forward .
        :return: A list representing a group of compatible keys
        :rtype list:
        """

        # handle a rollover at the apex of the wheel . when key_value is 12 or 112
        # we shift forward to 1 (major) or 101 (minor)
        if self.root_key_value == 12:
            up = Harmony._get_value(1)
        elif self.root_key_value == 112:
            up = Harmony._get_value(101)
        else:
            up = Harmony._get_value(self.root_key_value + 1)

        return up

    def minor(self):
        """ Fetches an adjacent key on the wheel (maj -> min or min -> maj).
        :return: A string
        :return:
        """

        # shift from major to minor
        if self.root_key_value < 100:
            return self._get_value(self.root_key_value + 100)
        # otherwise shift minor to major.
        else:
            return self._get_value(self.root_key_value - 100)
