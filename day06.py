# day 06


def get_input():
    with open("2022/day06 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def detect_start(stream, end):
    num_char = 0
    buffer = []

    for char in stream:
        num_char += 1
        if char in buffer:
            for c in list(buffer):
                if buffer.pop(0) == char:
                    break

        buffer.append(char)
        if len(buffer) == end:
            break

    return num_char


# part 1
def part_1():
    num_chars = 0
    lines = get_input()

    for line in lines:
        num_chars = detect_start(line, 4)
        # print(num_chars)

    return num_chars


# part 2
def part_2():
    num_chars = 0
    lines = get_input()

    for line in lines:
        num_chars = detect_start(line, 14)
        # print(num_chars)

    return num_chars


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
