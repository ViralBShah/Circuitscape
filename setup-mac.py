"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import pytz
pytz.zoneinfo = pytz.tzinfo
pytz.zoneinfo.UTC = pytz.UTC

from setuptools import setup

from circuitscape import __version__, __author__, __email__

PACKAGES = ['pyamg', 'wx']
INCLUDES = []

DATA_FILES = ['circuitscape/cs_logo.jpg', 'circuitscape']
OPTIONS = {'includes': INCLUDES, 
           'packages': PACKAGES,
           'argv_emulation': True,
           'plist': { 'CFBundleIdentifier': 'Circuitscape',
                      'CFBundleGetInfoString': 'Circuitscape: Circuit theoretic landscape connectivity',
                      'CFBundleDisplayName': 'Circuitscape',
                      'CFBundleIconFile': 'cs_logo.jpg',
                      'CFBundleIdentifier': 'org.circuitscape',
                      'CFBundleName': 'Circuitscape'
                     }
           }

setup(
    app             = ['bin/csgui.py'],
    setup_requires  = ['py2app'],
    data_files      = DATA_FILES,
    options         = {'py2app': OPTIONS},
    version         = __version__,
    author          = __author__,
    author_email    = __email__,
    )
