# Imbalanced Dataset Sampler

![license](https://img.shields.io/github/license/ufoym/imbalanced-dataset-sampler.svg)

A (PyTorch) weighted sampler for rebalancing the class distributions when sampling from the imbalanced dataset.

In many machine learning applications, we often come across datasets where some types of data may be seen more than other types. Take identification of rare diseases for example, there are probably more normal samples than disease ones. In these cases, we need to make sure that the trained model is not biased towards the class that has more data. As an example, consider a dataset where there are 5 disease images and 20 normal images. If the model predicts all images to be normal, its accuracy is 80%, and F1-score of such a model is 0.88. Therefore, the model has high tendency to be biased toward the ‘normal’ class.

To solve this problem, a widely adopted technique is called resampling. It consists of removing samples from the majority class (under-sampling) and / or adding more examples from the minority class (over-sampling). Despite the advantage of balancing classes, these techniques also have their weaknesses (there is no free lunch). The simplest implementation of over-sampling is to duplicate random records from the minority class, which can cause overfitting. In under-sampling, the simplest technique involves removing random records from the majority class, which can cause loss of information.

![resampling](https://user-images.githubusercontent.com/2270240/40656124-052ffdd2-6376-11e8-83f3-b174276599b0.png)

sample the entire dataset for one epoch and weigh your samples inversely to your class appearing probability
