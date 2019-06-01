# Neural Networks practice

## Usage

To use my code you need to install NumPy:

```bash
pip install numpy
```


## perceptron.py - Perceptron Learning Algorithm

Perceptron is the simplest neural network that uses supervised learning algorithm.

[How does it work? (Wikipedia)](https://en.wikipedia.org/wiki/Perceptron#Learning_algorithm)

Loop through all data points that aren't classified correctly:

- Check if the sign of the output is the different or 0. If it's the same, classify as correct.

![signs](https://github.com/piotsik/neural-networks/blob/master/images/perceptron1.png)

- Update *weight* and *bias*:

![weight](https://github.com/piotsik/neural-networks/blob/master/images/perceptron2.png)

![bias](https://github.com/piotsik/neural-networks/blob/master/images/perceptron3.png)

Use *xtable* list to instantiate data points, first number is output *y*, the list is input vector *x*:

```python
xtable = [
    Perceptron(1, np.array([-1, 1])),
    Perceptron(-1, np.array([0, -1])),
    Perceptron(1, np.array([10, 1])),
]
```

Each iteration:

```
x1: weights: [-1  1] bias: 1
x2: weights: [-1  2] bias: 0
x3: weights: [9 3] bias: 1
x1: weights: [8 4] bias: 2
x2: Classified correctly!
x3: Classified correctly!
x1: weights: [7 5] bias: 3
x1: Classified correctly!
```
