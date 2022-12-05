# day 03


def get_input():
    with open("2022/day03 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def score_items(items):
    sum = 0
    for item in items:
        ascii_value = ord(item)
        # print("ascii value: ", ord(item))
        if ascii_value >= 97:
            value = ascii_value - 96
            sum += ascii_value - 96
        else:
            value = ascii_value - 38
            sum += ascii_value - 38

    return sum


# part 1
def part_1():
    items = []
    lines = get_input()

    for line in lines:
        num_chars = len(line)
        if num_chars % 2 == 0:
            first_half = line[0 : num_chars // 2]
            second_half = line[num_chars // 2 :]
        else:
            print("ERROR!")

        common = list(set(first_half) & set(second_half))
        if len(common) != 1:
            print("ERROR!!")
        else:
            items += common[0]

    sum = score_items(items)

    return sum


# part 2
def part_2():
    items = []
    common = []
    lines = get_input()

    for i, line in enumerate(lines):
        if i % 3 == 0:
            if len(common) != 0:
                items += common[0]
            common = line
        else:
            common = list(set(common) & set(line))

    if len(common) != 0:
        items += common[0]

    sum = score_items(items)

    return sum


print("part 1 ", part_1())
print()

print("part 2 ", part_2())
