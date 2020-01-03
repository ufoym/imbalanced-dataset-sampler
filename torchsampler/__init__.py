__version__ = "0.1"
__author__ = "Ming"
__author_email__ = "a@ufoym.com"
__license__ = "MIT"
__homepage__ = "https://github.com/ufoym/imbalanced-dataset-sampler",
__doc__ = 'A (PyTorch) imbalanced dataset sampler for oversampling low frequent classes and undersampling high frequent ones.'

from torchsampler.imbalanced import ImbalancedDatasetSampler

__all__ = [
    'ImbalancedDatasetSampler',
]