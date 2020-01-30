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
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires = ['maz_metadata'],
    maz_cert='/src/addon-official/datajoint-dev.pem',
    entry_points={
        'maz.plugins': 'type = {}'.format(pkg_name)
    },
    # package_data={pkg_name: ['../{pkg}_data/{pkg}.sig'.format(pkg=pkg_name)]},
    # license='{"certificate":"DmK1aUc5jvBcaQpdOrcZhF0LmIfnYRqHsSCKjbgDAq0WMZ0HHxoSaDoiK/b7icpJ3kGMIpOdXxd7Sk7wD0WuJKzbLYOvXts6b6k8YYsG3A//HtbnFVNvB1w/PaCpWeu1obWhhQDdfAsihAicR9LxBuY9qweEaq9PLl9f0f72Dc0="}',
    # raphael='DmK1aUc5jvBcaQpdOrcZhF0LmIfnYRqHsSCKjbgDAq0WMZ0HHxoSaDoiK/b7icpJ3kGMIpOdXxd7Sk7wD0WuJKzbLYOvXts6b6k8YYsG3A//HtbnFVNvB1w/PaCpWeu1obWhhQDdfAsihAicR9LxBuY9qweEaq9PLl9f0f72Dc0=',
)