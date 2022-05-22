"""A setuptools based setup module."""

from pathlib import Path

from setuptools import setup

PATH_HERE = Path(__file__).parent

with open(PATH_HERE / 'requirements.txt', encoding='utf-8') as fp:
    requirements = [rq.rstrip() for rq in fp.readlines() if not rq.startswith('#')]
long_description = (PATH_HERE / 'README.md').read_text()

setup(
    name='torchsampler',
    use_scm_version=True,
    url="https://github.com/ufoym/imbalanced-dataset-sample",
    author="Ming, et al.",
    author_email="a@ufoym.com",
    license="MIT",
    description="A (PyTorch) imbalanced dataset sampler for oversampling low classes"
    "and undersampling high frequent ones.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['torchsampler'],
    keywords='sampler,pytorch,dataloader',
    setup_requires=['setuptools_scm'],
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
