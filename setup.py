"""A setuptools based setup module."""

import sys
from os import path

from setuptools import setup

try:
    from torchsampler import __about__ as about
except ImportError:
    # alternative https://stackoverflow.com/a/67692/4521646
    sys.path.append("torchsampler")
    import __about__ as about

PATH_HERE = path.abspath(path.dirname(__file__))

with open(path.join(PATH_HERE, 'requirements.txt'), encoding='utf-8') as fp:
    requirements = [rq.rstrip() for rq in fp.readlines() if not rq.startswith('#')]

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    name='torchsampler',
    version=about.__version__,
    url=about.__homepage__,
    author=about.__author__,
    author_email=about.__author_email__,
    license=about.__license__,
    description=about.__doc__,
    packages=['torchsampler'],
    keywords='sampler,pytorch,dataloader',
    install_requires=requirements,
    python_requires='>=3.6',
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
        'Programming Language :: Python :: 3',
    ],
)
