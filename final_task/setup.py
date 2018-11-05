from setuptools import setup

setup(
    name = 'pycalc',
    version = '1.0.0',
    author = 'Anton Charnichenka',
    author_email = 'antt0n.chern1chenk0@gmail.com',
    description = 'pure Python command line calculator',
    packages = ['pycalc'],
    entry_points = {'console_scripts': ['pycalc = pycalc.pycalc']},
    classifiers=["Programming Language :: Python :: 3.6", "Operating System :: Linux Mint"])
