import os
from setuptools import setup, find_packages

def read_requirements():
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join('.', 'requirements_full.txt')
    reqs = open(reqs_path, 'r')
    reqlist = [line.rstrip() for line in reqs]
    reqs.close()
    return reqlist

setup(
    name='neuronunit',
    version='0.19',
    author='Rick Gerkin',
    author_email='rgerkin@asu.edu',
    packages=find_packages(),
    url='http://github.com/scidash/neuronunit',
    license='MIT',
    description='A SciUnit library for data-driven testing of single-neuron physiology models.',
    long_description="",
    test_suite="neuronunit.unit_test.core_tests",
    install_requires=read_requirements()
    )
