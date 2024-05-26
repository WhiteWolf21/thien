import os
from distutils.core import setup
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='thien',
    version='0.1',
    description='HIHIHI',
    authors='Thien Huynh',
    author_email="thnhuynhngoc@gmail.com",
    license='MIT',
    package_dir={'thien':'src'},
    install_requires=required,
    url="https://github.com/WhiteWolf21/thien",
    package_data={
        'thien': ['**/*.txt', '**/*.t7', '**/*.pth', '**/*.json', '**/*.yaml', '**/*.yml']
    }
)