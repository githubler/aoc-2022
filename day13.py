# day 13

from icecream import ic


def get_input():
    with open("2022/day13 input.txt") as f:
        return [x.strip() for x in f.readlines()]


"""
def compare(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return 1

        if type(left[i]) is int and type(right[i]) is int:
            if left[i] < right[i]:
                return -1
            elif left[i] > right[i]:
                return 1
        else:
            if type(left[i]) is int:
                result = compare([left[i]], right[i])
            elif type(right[i]) is int:
                result = compare(left[i], [right[i]])
            else:
                result = compare(left[i], right[i])

            if result != 0:
                return result

    if len(left) < len(right):
        return -1
    else:
        return 0
"""


def compare(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    else:
        if type(left) is int:
            return compare([left], right)
        elif type(right) is int:
            return compare(left, [right])

    for l, r in zip(left, right):
        result = compare(l, r)
        if result != 0:
            return result

    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


# part 1
def part_1():
    sum_indices = 0

    input = get_input()
    for index, i in enumerate(range(0, len(input), 3), start=1):
        left = eval(input[i])
        right = eval(input[i + 1])
        # ic(left)
        # ic(right)

        if compare(left, right) < 0:
            sum_indices += index
            # ic("YES")
        # else:
        # ic("NO")

    return sum_indices


def get_input_2():
    return open("2022/day13 input.txt").read().split()


# part 2
def part_2():
    result = 0

    index_divider_1 = 1
    index_divider_2 = 2
    divider_1 = [[2]]
    divider_2 = [[6]]

    packets = list(map(eval, get_input_2()))
    for packet in packets:
        if compare(packet, divider_1) < 0:
            index_divider_1 += 1
            index_divider_2 += 1
        elif compare(packet, divider_2) < 0:
            index_divider_2 += 1

    return index_divider_1 * index_divider_2


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
