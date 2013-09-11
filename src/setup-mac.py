"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import pytz
pytz.zoneinfo = pytz.tzinfo
pytz.zoneinfo.UTC = pytz.UTC

from setuptools import setup

INCLUDES = []
PACKAGES = ['wx', 'PythonCard', 'numpy', 'scipy', 'pyamg']

DATA_FILES = ['cs_gui.rsrc.py', 'cs_verify.py', 'cs_util.py', 'gapdt.py', 'cs_compute.py', 'cs_logo.jpg', 'verify', 'verify/1', 'verify/2', 'verify/3', 'verify/4', 'verify/5']
OPTIONS = {'packages': PACKAGES, 
           'argv_emulation' : True,
           'plist': { 'CFBundleIdentifier': 'Circuitscape',
                      'CFBundleGetInfoString': 'Circuitscape: Circuit theoretic landscape connectivity',
                      'CFBundleDisplayName': 'Circuitscape',
                      'CFBundleIconFile': 'cs_logo.jpg',
                      'CFBundleIdentifier': 'org.circuitscape',
                      'CFBundleName': 'Circuitscape'
                     }
           }
#Now also compile cs_run.py.  compiling it first ensures that dependencies needed for cs_gui also included.
# setup(
#     app=['cs_run.py'],
#     setup_requires=['py2app'],
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     version='3.5.7',
#     author='Brad McRae and Viral B. Shah',
#     author_email='mcrae@circuitscape.org'
# )

setup(
    app=['cs_gui.py'],
    setup_requires=['py2app'],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    version='3.5.8',
    author='Brad McRae and Viral B. Shah',
    author_email='mcrae@circuitscape.org'
    )