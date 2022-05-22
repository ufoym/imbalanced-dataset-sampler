import sys

if sys.version_info < (3, 8):
    from importlib_metadata import PackageNotFoundError, version
else:
    from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("torchsampler")
except PackageNotFoundError:
    # package is not installed (i.e. we're probably in the build process itself)
    pass
__version__ = "0.1.1"
__author__ = "Ming, et al."
__author_email__ = "a@ufoym.com"
__license__ = "MIT"
__homepage__ = "https://github.com/ufoym/imbalanced-dataset-sampler"
__doc__ = "A (PyTorch) imbalanced dataset sampler for oversampling low frequent classes" \
          " and undersampling high frequent ones."

__all__ = [
    "__author__",
    "__author_email__",
    "__doc__",
    "__homepage__",
    "__license__",
    "__version__",
]
