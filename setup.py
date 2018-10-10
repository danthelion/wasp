from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wasp_spotify_bindings',
    version='0.0.1',
    description='Python wrapper to control your Spotify client on MacOS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/danthelion/wasp',
    author='Daniel Palma',
    author_email='danivgy@gmail.com',
    keywords='spotify api',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
