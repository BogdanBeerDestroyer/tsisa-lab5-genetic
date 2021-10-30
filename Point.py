import numpy as np
import random


def fun(x, y):
    return np.cos(x) * np.cos(y)


class Point:
    mut_prop = 0.25
    mut_coef = 0.05
    x1 = -2
    x2 = 2
    y1 = -2
    y2 = 2

    def __init__(self, x=random.uniform(x1, x2),
                 y=random.uniform(y1, y2)):
        self.x = x
        self.y = y

    def fun_val(self):
        return fun(self.x, self.y)

    def crossing(self, oth):
        return [
            Point(self.x, oth.y),
            Point(oth.x, self.y)
        ]

    def mutation(self):
        num = random.uniform(0, 1)
        if num <= Point.mut_prop:
            if num <= Point.mut_prop / 2:
                self.x -= Point.mut_coef * (Point.x2 - Point.x1)
            else:
                self.x += Point.mut_coef * (Point.x2 - Point.x1)
        num = random.uniform(0, 1)
        if num <= Point.mut_prop:
            if num <= Point.mut_prop / 2:
                self.y -= Point.mut_coef * (Point.y2 - Point.y1)
            else:
                self.y += Point.mut_coef * (Point.y2 - Point.y1)
        if self.x > Point.x2:
            self.x = Point.x2
        if self.x < Point.x1:
            self.x = Point.x1
        if self.y > Point.y2:
            self.y = Point.y2
        if self.y < Point.y1:
            self.y = Point.y1

    def print(self):
        print(self.x, "    ", self.y)
