import random
from Point import Point


class Generation:
    points_num = 4

    def __init__(self, prev=None):
        if prev is None:
            self.points = [Point(random.uniform(Point.x1, Point.x2),
                                 random.uniform(Point.y1, Point.y2)) for i in
                           range(Generation.points_num)]
        else:
            sorted_prev = sorted(prev.points, key=lambda p: p.fun_val(), reverse=True)
            self.points = sorted_prev[0].crossing(sorted_prev[1]) + sorted_prev[0].crossing(sorted_prev[1])
            for i in self.points:
                i.mutation()

    @classmethod
    def next_gen(cls, prev):
        obj = cls(prev)
        return obj

    def print_gen(self):
        for i in range(Generation.points_num):
            print(f"{self.points[i].x},   {self.points[i].y}")
