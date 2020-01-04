# Imbalanced Dataset Sampler

![license](https://img.shields.io/github/license/ufoym/imbalanced-dataset-sampler.svg)


- [Introduction](#Introduction)
- [Usage](#Usage)
- [Example](#Example)
  - [Imbalanced MNIST Dataset](#Example)
- [Contributing](#Contributing)
- [Licensing](#Licensing)

---

<a name="Introduction"/>

## Introduction

In many machine learning applications, we often come across datasets where some types of data may be seen more than other types. Take identification of rare diseases for example, there are probably more normal samples than disease ones. In these cases, we need to make sure that the trained model is not biased towards the class that has more data. As an example, consider a dataset where there are 5 disease images and 20 normal images. If the model predicts all images to be normal, its accuracy is 80%, and F1-score of such a model is 0.88. Therefore, the model has high tendency to be biased toward the ‘normal’ class.

To solve this problem, a widely adopted technique is called resampling. It consists of removing samples from the majority class (under-sampling) and / or adding more examples from the minority class (over-sampling). Despite the advantage of balancing classes, these techniques also have their weaknesses (there is no free lunch). The simplest implementation of over-sampling is to duplicate random records from the minority class, which can cause overfitting. In under-sampling, the simplest technique involves removing random records from the majority class, which can cause loss of information.

![resampling](https://user-images.githubusercontent.com/2270240/40656410-e0baa230-6376-11e8-8904-c092fb38fcdc.png)

In this repo, we implement an easy-to-use PyTorch sampler `ImbalancedDatasetSampler` that is able to
- rebalance the class distributions when sampling from the imbalanced dataset
- estimate the sampling weights automatically
- avoid creating a new balanced dataset
- mitigate overfitting when it is used in conjunction with data augmentation techniques

<p align="center">
  <img src="https://user-images.githubusercontent.com/2270240/40677251-b08f504a-63af-11e8-9653-f28e973a5664.png">
</p>


<a name="Usage"/>

## Usage

For a simple start install the package via one of following ways:
```bash
python setup.py install
pip install .
```


Simply pass an `ImbalancedDatasetSampler` for the parameter `sampler` when creating a `DataLoader`.
For example:

```python
from torchsampler import ImbalancedDatasetSampler

train_loader = torch.utils.data.DataLoader(
    train_dataset, 
    sampler=ImbalancedDatasetSampler(train_dataset),
    batch_size=args.batch_size, 
    **kwargs
)
```

Then in each epoch, the loader will sample the entire dataset and weigh your samples inversely to your class appearing probability.


<a name="Example"/>

## Example: Imbalanced MNIST Dataset

Distribution of classes in the imbalanced dataset:
<p align="center">
  <img src="https://user-images.githubusercontent.com/2270240/40678060-03c6eb9a-63b2-11e8-9a81-c61c665240e3.png">
</p>

With Imbalanced Dataset Sampler:
<p align="center">
  <img src="https://user-images.githubusercontent.com/2270240/40678100-1e543f12-63b2-11e8-9c05-3b168c3fb39f.png">
  (left: test acc in each epoch; right: confusion matrix)
</p>

Without Imbalanced Dataset Sampler:
<p align="center">
  <img src="https://user-images.githubusercontent.com/2270240/40678099-1e0a481c-63b2-11e8-9ec8-f2ac4bf7a637.png">
  (left: test acc in each epoch; right: confusion matrix)
</p>

Note that there are significant improvements for minor classes such as `2` `6` `9`, while the accuracy of the other classes is preserved.

<a name="Contributing"/>

## Contributing

We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so without any further discussion. If you plan to contribute new features, utility functions or extensions, please first open an issue and discuss the feature with us.

<a name="Licensing"/>

## Licensing

[MIT licensed](https://github.com/ufoym/imbalanced-dataset-sampler/blob/master/LICENSE).
