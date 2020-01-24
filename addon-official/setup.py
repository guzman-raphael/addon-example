import setuptools
from os import path

pkg_name = "mzaddon_type_student"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.abspath(path.dirname(__file__)), pkg_name, 'meta.py')) as f:
    exec(f.read())

setuptools.setup(
    name=pkg_name,
    version=__version__,
    author="Raphael Guzman",
    author_email="raphael.h.guzman@gmail.com",
    description="Official Addon example.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guzman-raphael/addon-example",
    entry_points={'maz.plugins': 'type = {}'.format(pkg_name)},
    packages=setuptools.find_packages(),
    # package_data={pkg_name: ['../{pkg}_data/{pkg}.sig'.format(pkg=pkg_name)]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='{"certificate":"s6kIfnzrD5DkGkkYXXcJLA0klnavt1ts8j6b+tVHZkLo1kHsNMbm3ZSfL85bAc0/quTjBFd7Z3Xqlav/4lGnP7OV98xn/xNHfEFHbgi1mJ2OIBgYZMvQ1fahtV22HKD4x2ca6MI7/B2mE55e4JRksMEtAYjYVn2DJtjdfjA04Hs="}',
    raphael='s6kIfnzrD5DkGkkYXXcJLA0klnavt1ts8j6b+tVHZkLo1kHsNMbm3ZSfL85bAc0/quTjBFd7Z3Xqlav/4lGnP7OV98xn/xNHfEFHbgi1mJ2OIBgYZMvQ1fahtV22HKD4x2ca6MI7/B2mE55e4JRksMEtAYjYVn2DJtjdfjA04Hs=',
)