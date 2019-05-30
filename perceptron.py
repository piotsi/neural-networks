import numpy as np


class Perceptron:

    b = 0
    w = np.array([0, 0])
    data_pts_amm = 0

    def __init__(self, y, el):
        self.y = y
        self.el = el
        self.correct = False
        Perceptron.data_pts_amm += 1
        self.number = Perceptron.data_pts_amm

    def is_correct(self):
        if self.correct:
            return True
        return False

    def update(self):
        Perceptron.w += np.dot(self.y, self.el)
        Perceptron.b += self.y

    def check(self):
        print(self.__str__(), end=': ')
        v = np.dot(self.el, self.w) + Perceptron.b
        if v == 0 or np.sign(v) != np.sign(self.y):
            self.update()
            print('weights: {} bias: {}'.format(x.w, x.b))
        else:
            self.correct = True
            print('Classified correctly!')

    def __str__(self):
        return 'x{}'.format(self.number)

xtable = [
    Perceptron(1, np.array([-1, 1])),
    Perceptron(-1, np.array([0, -1])),
    Perceptron(1, np.array([10, 1])),
]

while not all(x.correct for x in xtable):
    for x in xtable:
        if not x.correct:
            x.check()
