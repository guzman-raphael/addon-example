#!/bin/sh

cd $1
rm -R build dist *.egg-info
python setup.py sdist bdist_wheel
# python -m twine upload -s -i "DataJoint Dev" --repository-url https://test.pypi.org/legacy/ dist/*
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# rm -R build dist *.egg-info
