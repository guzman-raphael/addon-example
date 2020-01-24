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
    package_data={pkg_name: ['../{pkg}_data/{pkg}.sig'.format(pkg=pkg_name)]},
    # packages=['mypkg'],
    # packages=['mzaddon_type_student', 'cert'],
    # package_dir={'.': pkg_name},
    # package_data={'': ['*.sig']},
    # packages=['mzaddon_type_student', 'cert'],
    # package_data={'': ['mzaddon_type_student.sig', 'mzaddon_type_student2.sig'],
    #               'mzaddon_type_student':['mzaddon_type_student3.sig']},
    # data_files=[('.',['mzaddon_type_student.sig']),
    #             ('cert',['cert/mzaddon_type_student2.sig'])],
    # include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='{"certificate":"mDpXHIay8/9XKVTzwcIq8WHUMZFqE7/v1NgZWVvQCcXw7W6Afk8tZ2lrfMlZBz77bz1L6kd3AaErrs5CAlat1uocYKhvUVHKqjbObETXqP2xJAHDoZufKZsASjs78IjhBgZI5uH1Q8ZMiFSrf6MhTicq+er8G++FMG6mz8+Wf1Y="}',
)