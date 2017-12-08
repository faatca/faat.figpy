import os
import re
from setuptools import setup


def read(*names, **kwargs):
    path = os.path.join(os.path.dirname(__file__), *names)
    with open(path, encoding='utf-8') as f:
        return f.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='faat.figpy',
    version=find_version('faat', 'figpy', '__init__.py'),

    description="Simple configuration library using python syntax",
    long_description=read('README.txt'),

    url='https://www.faat.ca',

    author='Aaron Milner',
    author_email='aaron.milner@gmail.com',

    license='Proprietary',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=[],

    packages=['faat.figpy'],
    install_requires=[],
)