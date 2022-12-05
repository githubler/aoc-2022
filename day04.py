# day 04


def get_input():
    with open("2022/day04 input.txt") as f:
        return [x.strip() for x in f.readlines()]


# part 1
def part_1():
    num_fully_contains = 0
    lines = get_input()

    for line in lines:
        assignment_1, assignment_2 = line.split(",")
        first_a1, second_a1 = assignment_1.split("-")
        first_a2, second_a2 = assignment_2.split("-")

        if (
            (int(first_a1) <= int(first_a2))
            and (int(second_a1) >= int(second_a2))
            and (int(second_a2) >= int(first_a1))
        ):
            num_fully_contains += 1
        elif (
            (int(first_a2) <= int(first_a1))
            and (int(second_a2) >= int(second_a1))
            and (int(second_a1) >= int(first_a2))
        ):
            num_fully_contains += 1

    return num_fully_contains


# part 2
def part_2():
    num_fully_contains = 0
    lines = get_input()

    for i, line in enumerate(lines):
        assignment_1, assignment_2 = line.split(",")
        first_pair = assignment_1.split("-")
        second_pair = assignment_2.split("-")

        first_a1 = int(first_pair[0])
        first_a2 = int(first_pair[1])
        second_a1 = int(second_pair[0])
        second_a2 = int(second_pair[1])

        if (second_a1 <= first_a2) and (second_a1 >= first_a1):
            num_fully_contains += 1
        elif (second_a2 >= first_a1) and (second_a2 <= first_a1):
            num_fully_contains += 1
        elif (first_a1 <= second_a2) and (first_a1 >= second_a1):
            num_fully_contains += 1
        elif (first_a2 >= second_a1) and (first_a2 <= second_a1):
            num_fully_contains += 1

    return num_fully_contains


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
