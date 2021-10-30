from statistics import mean
import numpy as np
import Point
from gen import Generation
from prettytable import PrettyTable
import matplotlib.pyplot as plt


def gen_to_table(gen, table, num_of_gen, dots_for_plot):
    values = [Point.fun(i.x, i.y) for i in gen.points]
    table.add_row([num_of_gen, gen.points[0].x, gen.points[0].y, values[0], mean(values), max(values)])
    dots_for_plot[0].append(num_of_gen)
    dots_for_plot[1].append(max(values))
    for i, j in zip(gen.points[1::], values[1::]):
        table.add_row([num_of_gen, i.x, i.y, j, "", ""])


def graph(x1, x2, y1, y2):
    g3d = plt.figure(figsize=(10, 10)).add_subplot(projection='3d')
    x = np.arange(x1, x2, 0.1)
    y = np.arange(y1, y2, 0.1)
    xg, yg = np.meshgrid(x, y)
    zg = Point.fun(xg, yg)
    g3d.set_xlabel('x')
    g3d.set_ylabel('y')
    g3d.set_zlabel('z')
    g3d.plot_surface(xg, yg, zg, cmap='plasma')
    plt.show()


def genetic_search(number_of_gens):
    file = open("results/results.txt", "w")
    dots_for_plot = [[], []]
    gen = Generation()
    table = PrettyTable()
    table.field_names = ["Num of gen", "x", "y", "Fit value", "mean", "best"]
    gen_to_table(gen, table, 0, dots_for_plot)
    for i in range(number_of_gens + 1):
        gen = Generation.next_gen(gen)
        gen_to_table(gen, table, i, dots_for_plot)
    output = table.get_string()
    file.write(output)
    print(table)
    plt.plot(dots_for_plot[0], dots_for_plot[1], 'ro')
    plt.show()



def main():
    genetic_search(100)
    graph(Point.Point.x1, Point.Point.x2, Point.Point.y1, Point.Point.y2)


if __name__ == "__main__":
    main()
