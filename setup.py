"""A setuptools based setup module."""

from pathlib import Path

from setuptools import setup

try:
    from torchsampler import __about__ as about
except ImportError:
    # alternative https://stackoverflow.com/a/67692/4521646
    sys.path.append("torchsampler")
    import __about__ as about

PATH_HERE = Path(__file__).parent

with open(PATH_HERE / 'requirements.txt', encoding='utf-8') as fp:
    requirements = [rq.rstrip() for rq in fp.readlines() if not rq.startswith('#')]
long_description = (PATH_HERE / 'README.md').read_text()

setup(
    name='torchsampler',
    version=about.__version__,
    url=about.__homepage__,
    author=about.__author__,
    author_email=about.__author_email__,
    license=about.__license__,
    description=about.__doc__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['torchsampler'],
    keywords='sampler,pytorch,dataloader',
    install_requires=requirements,
    python_requires='>=3.6',
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
