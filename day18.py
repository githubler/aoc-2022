# day 18

import numpy as np
from scipy import ndimage

# import matplotlib.pyplot as plt


# max input is 21 -> move input +1 for the edge cases
dim = 23


def get_input():
    with open("2022/day18 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def test_neighbours(shape, x, y, z) -> int:
    global dim

    area = 0
    if shape[x][y][z] > 0:
        if x > 0 and shape[x - 1][y][z] < 1:
            area += 1
        if x < dim and shape[x + 1][y][z] < 1:
            area += 1

        if y > 0 and shape[x][y - 1][z] < 1:
            area += 1
        if y < dim and shape[x][y + 1][z] < 1:
            area += 1

        if z > 0 and shape[x][y][z - 1] < 1:
            area += 1
        if z < dim and shape[x][y][z + 1] < 1:
            area += 1

    return area


def get_surface_area(shape):
    area = 0
    for x in range(len(shape)):
        for y in range(len(shape[x])):
            for z in range(len(shape[x][y])):
                area += test_neighbours(shape, x, y, z)

    return area


def build_solid_shape(shape):
    global dim
    solid_shape = np.zeros((dim + 1, dim + 1, dim + 1)).astype(np.uint8)

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection="3d")
    # z, x, y = shape.nonzero()
    # ax.scatter(x, y, z, c=z, alpha=1)
    # plt.show()

    markers = np.zeros_like(shape).astype(np.int16)
    markers[0, 0, 0] = -1
    markers[10, 10, 10] = 1
    solid_shape = ndimage.watershed_ift(shape.astype(np.uint8), markers)

    return solid_shape


def fill_shape(shape):
    for line in get_input():
        i, j, k = line.split(",")
        i, j, k = int(i) + 1, int(j) + 1, int(k) + 1
        shape[int(i)][int(j)][int(k)] = 1

    return shape


# part 1
def part_1():
    global dim
    area = 0
    shape = np.zeros((dim + 1, dim + 1, dim + 1))
    shape = fill_shape(shape)

    area = get_surface_area(shape)

    return area


# part 2
def part_2():
    global dim

    area = 0
    shape = np.zeros((dim + 1, dim + 1, dim + 1)).astype(np.uint8)
    shape = fill_shape(shape)

    solid_shape = build_solid_shape(shape)
    # need to add the original shape :-(
    solid_shape = fill_shape(solid_shape)

    area = get_surface_area(solid_shape)

    return area


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
