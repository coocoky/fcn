#!/usr/bin/env python

from distutils.command.build_py import build_py as BuildPyCommand
import os
import os.path as osp
import shlex
import subprocess
import sys
import tempfile

from setuptools import find_packages
from setuptools import setup


version = '3.2.0'


if sys.argv[-1] == 'release':
    commands = [
        'python setup.py sdist',
        'twine upload dist/fcn-{0}.tar.gz'.format(version),
        'git tag v{0}'.format(version),
        'git push origin master --tag',
    ]
    for cmd in commands:
        subprocess.call(shlex.split(cmd))
    sys.exit(0)


setup(
    name='fcn',
    version=version,
    packages=find_packages(),
    scripts=['scripts/fcn_forward.py', 'scripts/fcn_install_trained_data.py'],
    install_requires=open('requirements.txt').readlines(),
    description='Fully Convolutional Networks',
    long_description=open('README.rst').read(),
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/fcn',
    license='MIT',
    keywords='machine-learning',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
