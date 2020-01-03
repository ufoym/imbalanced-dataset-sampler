__version__ = "0.1"
__author__ = "Ming"
__author_email__ = "a@ufoym.com"
__license__ = "MIT"
__homepage__ = "https://github.com/ufoym/imbalanced-dataset-sampler",
__doc__ = 'A (PyTorch) imbalanced dataset sampler for oversampling low frequent classes and undersampling high frequent ones.'

try:
    # This variable is injected in the __builtins__ by the build
    # process. It used to enable importing subpackages of skimage when
    # the binaries are not built
    __LIGHTNING_SETUP__
except NameError:
    __LIGHTNING_SETUP__ = False

if __LIGHTNING_SETUP__:
    import sys
    sys.stderr.write('Partial import during the build process.\n')
else:
    from torchsampler.imbalanced import ImbalancedDatasetSampler

    __all__ = [
        'ImbalancedDatasetSampler',
    ]
