# day 05

import re
from collections import deque


def get_input():
    with open("2022/day05 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def parse_input():
    lines = get_input()
    line = lines.pop(0)

    while line != "":
        line = lines.pop(0)

    #
    # stack test data
    #     [D]
    # [N] [C]
    # [Z] [M] [P]
    #  1   2   3

    # move 1 from 2 to 1
    # move 3 from 1 to 3
    # move 2 from 2 to 1
    # move 1 from 1 to 2
    # stacks = []
    # stack = deque()
    # stack.append("Z")
    # stack.append("N")
    # stacks.append(stack)
    # stack = deque()
    # stack.append("M")
    # stack.append("C")
    # stack.append("D")
    # stacks.append(stack)
    # stack = deque()
    # stack.append("P")
    # stacks.append(stack)

    #
    # stack input data
    #         [M]     [B]             [N]
    # [T]     [H]     [V] [Q]         [H]
    # [Q]     [N]     [H] [W] [T]     [Q]
    # [V]     [P] [F] [Q] [P] [C]     [R]
    # [C]     [D] [T] [N] [N] [L] [S] [J]
    # [D] [V] [W] [R] [M] [G] [R] [N] [D]
    # [S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
    # [N] [M] [F] [D] [R] [C] [W] [T] [M]
    #  1   2   3   4   5   6   7   8   9

    stacks = []
    stack = deque()
    stack.append("N")
    stack.append("S")
    stack.append("D")
    stack.append("C")
    stack.append("V")
    stack.append("Q")
    stack.append("T")
    stacks.append(stack)

    stack = deque()
    stack.append("M")
    stack.append("F")
    stack.append("V")
    stacks.append(stack)

    stack = deque()
    stack.append("F")
    stack.append("Q")
    stack.append("W")
    stack.append("D")
    stack.append("P")
    stack.append("N")
    stack.append("H")
    stack.append("M")
    stacks.append(stack)

    stack = deque()
    stack.append("D")
    stack.append("Q")
    stack.append("R")
    stack.append("T")
    stack.append("F")
    stacks.append(stack)

    stack = deque()
    stack.append("R")
    stack.append("F")
    stack.append("M")
    stack.append("N")
    stack.append("Q")
    stack.append("H")
    stack.append("V")
    stack.append("B")
    stacks.append(stack)

    stack = deque()
    stack.append("C")
    stack.append("F")
    stack.append("G")
    stack.append("N")
    stack.append("P")
    stack.append("W")
    stack.append("Q")
    stacks.append(stack)

    stack = deque()
    stack.append("W")
    stack.append("F")
    stack.append("R")
    stack.append("L")
    stack.append("C")
    stack.append("T")
    stacks.append(stack)

    stack = deque()
    stack.append("T")
    stack.append("Z")
    stack.append("N")
    stack.append("S")
    stacks.append(stack)

    stack = deque()
    stack.append("M")
    stack.append("S")
    stack.append("D")
    stack.append("J")
    stack.append("R")
    stack.append("Q")
    stack.append("H")
    stack.append("N")
    stacks.append(stack)

    commands = lines

    return stacks, commands


# part 1
def part_1():
    PATTERN = re.compile(r"move (?P<num>\d+) from (?P<from>\d+) to (?P<to>\d+)")

    result = ""
    stacks, commands = parse_input()

    for command in commands:
        num, from_stack, to_stack = 0, 0, 0
        if (m := PATTERN.match(command)) is not None:
            num, from_stack, to_stack = int(m["num"]), int(m["from"]), int(m["to"])

            # move item
            for i in range(num):
                cargo = stacks[from_stack - 1].pop()
                stacks[to_stack - 1].append(cargo)

    for stack in stacks:
        result += stack.pop()

    return result


# part 2
def part_2():
    PATTERN = re.compile(r"move (?P<num>\d+) from (?P<from>\d+) to (?P<to>\d+)")

    result = ""
    stacks, commands = parse_input()

    for command in commands:
        num, from_stack, to_stack = 0, 0, 0
        if (m := PATTERN.match(command)) is not None:
            num, from_stack, to_stack = int(m["num"]), int(m["from"]), int(m["to"])

            # move item
            storage = deque()
            for i in range(num):
                cargo = stacks[from_stack - 1].pop()
                storage.append(cargo)

            for i in range(num):
                cargo = storage.pop()
                stacks[to_stack - 1].append(cargo)

    for stack in stacks:
        result += stack.pop()

    return result


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
