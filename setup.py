import os
from distutils.core import setup

NAME = 'harmonic-shuffle'
VERSION = '0.0.1'

setup(
    name = 'harmonic_shuffle',
    version = '0.0.1',
    author = 'Jesse Ward',
    author_email = 'jesse@jesseward.com',
    description = ('Generate playlists based on compatible harmonies using the wheel of fifths / camelot wheel'),
    license = 'MIT',
    url = 'https://github.com/jesseward/harmonic-shuffle',
    scripts = ['scripts/harmonic-shuffle.py'],
    packages=['harmonic_shuffle'],
)