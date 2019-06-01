# Neural Networks practice

## Usage

To use my code you need to install NumPy:

```bash
pip install numpy
```


## perceptron.py - Perceptron Learning Algorithm

Perceptron is the simplest neural network that uses supervised learning algorithm.
[How does it work?](https://en.wikipedia.org/wiki/Perceptron#Learning_algorithm)

Use *xtable* list to initialize data points, first number is output *y*, the list is input vector *x*:

```python
xtable = [
    Perceptron(1, np.array([-1, 1])),
    Perceptron(-1, np.array([0, -1])),
    Perceptron(1, np.array([10, 1])),
]
```

Each iteration:

```bash
x1: weights: [-1  1] bias: 1
x2: weights: [-1  2] bias: 0
x3: weights: [9 3] bias: 1
x1: weights: [8 4] bias: 2
x2: Classified correctly!
x3: Classified correctly!
x1: weights: [7 5] bias: 3
x1: Classified correctly!
```
