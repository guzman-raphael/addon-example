import setuptools
from os import path

pkg_name = "maz_metadata"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.abspath(path.dirname(__file__)), pkg_name, '__init__.py')) as f:
    exec(f.read())

setuptools.setup(
    name=pkg_name,
    version=__version__,
    author="Raphael Guzman",
    author_email="raphael.h.guzman@gmail.com",
    description="Maz setup addon example.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guzman-raphael/addon-example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "distutils.setup_keywords": [
            "maz_privkey_path = maz_metadata:assert_string",
            # "maz_cert = setuptools.dist:assert_string_list",
        ],
        "egg_info.writers": [
            "maz_privkey_path.sig = maz_metadata:write_arg",
            # "maz_cert.sig = setuptools.command.egg_info:write_arg",
        ],
    },
    install_requires=['cryptography'],
)