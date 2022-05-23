import sys

if sys.version_info < (3, 8):
    from importlib_metadata import distribution, PackageNotFoundError
else:
    from importlib.metadata import distribution, PackageNotFoundError

import warnings

warnings.warn(
    "Use importlib.metadata.distribution('torchsampler').metadata instead of torchsampler.__about__.",
    category=DeprecationWarning
)

try:
    _m = distribution('torchsampler').metadata
    __version__ = _m['version']
    __author__ = _m['author']
    __author_email__ = _m['author-email']
    __license__ = _m['license']
    __homepage__ = _m['homepage']
    __doc__ = _m['summary']
    del _m
except PackageNotFoundError:
    # package is not installed (i.e. we're probably in the build process itself)
    pass

del sys, distribution, PackageNotFoundError, warnings

__all__ = [
    "__author__",
    "__author_email__",
    "__doc__",
    "__homepage__",
    "__license__",
    "__version__",
]
