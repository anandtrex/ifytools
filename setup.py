from setuptools import setup

__version__ = '0.1.0'
__author__ = 'Anand Subramoney'

"""
This file installs the ifytools package.
For updating the version, update __version__ in ifytools/__init__.py
"""

setup(
    name="ifytools",
    version=__version__,
    install_requires=['randomgen'],
    packages=['ifytools'],
    author="Anand Subramoney",
    author_email="anand@igi.tugraz.at",
    description="This module provides some functional tools (primarily related to ML)",
    provides=['ifytools'],

)
