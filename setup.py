from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, 'ncaa_select_picks', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='ncaa_select_picks',
    version=version['__version__'],
    description=('NCAA March Madness Men\'s Basketball Bracket Selection Tool'),
    long_description=('This python package serves to provide a fun selection tool for March Madness Men\'s Basketball bracket selections. This uses a simple algorithm to help those who want to complete a bracket.'),
    author='Luke Pajer',
    author_email='luke.pajer@gmail.com',
    url='https://github.com/The-Geology-Guy/ncaa_select_picks',
    download_url='https://github.com/The-Geology-Guy/ncaa_select_picks/archive/refs/tags/v0.0.3.tar.gz',
    license='MIT',
    packages=['ncaa_select_picks'],
    install_requires=[
        'numpy',
        'IPython',
        'random',
    ],
    include_package_data=True,
    classifiers=[
        'Topic :: Games/Entertainment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',],
    )
