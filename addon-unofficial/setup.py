# name = "maz"

import setuptools
from os import path

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.abspath(path.dirname(__file__)), 'mzaddon_user', 'version.py')) as f:
    exec(f.read())

setuptools.setup(
    name="mzaddon_user",
    version=__version__,
    author="Raphael Guzman",
    author_email="raphael.h.guzman@gmail.com",
    description="Unofficial Addon example.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guzman-raphael/addon-example",
    packages=setuptools.find_packages(),
    entry_points={'maz.plugins': 'user = mzaddon_user'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)