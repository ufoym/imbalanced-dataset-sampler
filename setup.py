"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from os import path
from setuptools import setup
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines, and accepts an argument
#  to specify the text encoding Python 3 only projects can skip this import
from io import open

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

builtins.__LIGHTNING_SETUP__ = True
PATH_HERE = path.abspath(path.dirname(__file__))

import torchsampler

with open(path.join(PATH_HERE, 'requirements.txt'), encoding='utf-8') as fp:
    requirements = [rq.rstrip() for rq in fp.readlines() if not rq.startswith('#')]

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    name='torchsampler',
    version=torchsampler.__version__,
    url=torchsampler.__homepage__,

    author=torchsampler.__author__,
    author_email=torchsampler.__author_email__,
    license=torchsampler.__license__,
    description=torchsampler.__doc__,

    packages=['torchsampler'],

    keywords='sampler',
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
