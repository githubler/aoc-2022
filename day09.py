# day 09

# from icecream import ic


def get_input():
    with open("2022/day09 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def move_tail(head, tail):
    if (abs(head[0] - tail[0]) > 1) and (abs(head[1] - tail[1]) > 1):
        x = tail[0] + 1 if tail[0] < head[0] else tail[0] - 1
        y = tail[1] + 1 if tail[1] < head[1] else tail[1] - 1
        tail = (x, y)
    elif abs(head[0] - tail[0]) > 1:
        x = tail[0] + 1 if tail[0] < head[0] else tail[0] - 1
        y = head[1]
        tail = (x, y)
    elif abs(head[1] - tail[1]) > 1:
        x = head[0]
        y = tail[1] + 1 if tail[1] < head[1] else tail[1] - 1
        tail = (x, y)

    return tail


# part 1
def part_1():
    trace = set()
    head = (0, 0)
    tail = (0, 0)

    for line in get_input():
        direction, steps = line.split()

        for step in range(int(steps)):
            match direction:
                case "R":
                    head = (head[0] + 1, head[1])
                case "L":
                    head = (head[0] - 1, head[1])
                case "U":
                    head = (head[0], head[1] + 1)
                case "D":
                    head = (head[0], head[1] - 1)

            tail = move_tail(head, tail)
            trace.add(tail)

    return len(trace)


# part 2
def part_2():
    trace = set()
    knot = [(0, 0) for _ in range(10)]

    for line in get_input():
        direction, steps = line.split()

        for step in range(int(steps)):
            match direction:
                case "R":
                    knot[0] = (knot[0][0] + 1, knot[0][1])
                case "L":
                    knot[0] = (knot[0][0] - 1, knot[0][1])
                case "U":
                    knot[0] = (knot[0][0], knot[0][1] + 1)
                case "D":
                    knot[0] = (knot[0][0], knot[0][1] - 1)

            for i in range(9):
                knot[i + 1] = move_tail(knot[i], knot[i + 1])

            # ic(knot[9])
            trace.add(knot[9])

    return len(trace)


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
