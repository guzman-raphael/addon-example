import setuptools
from os import path

pkg_name = "mzaddon_user_raphael"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.abspath(path.dirname(__file__)), pkg_name, 'version.py')) as f:
    exec(f.read())

setuptools.setup(
    name=pkg_name,
    version=__version__,
    author="Raphael Guzman",
    author_email="raphael.h.guzman@gmail.com",
    description="Unofficial Addon example.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guzman-raphael/addon-example",
    packages=setuptools.find_packages(),
    entry_points={'maz.plugins_user': 'raphael = {}'.format(pkg_name)},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)