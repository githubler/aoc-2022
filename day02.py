# day 02


def get_input():
    with open("2022/day02 input.txt") as f:
        return [x.strip() for x in f.readlines()]


# part 1
def part_1():
    lines = get_input()
    # print(lines)

    # A/X = Rock = 1
    # B/Y = Paper = 2
    # C/Z = Scissor = 3
    my_score = 0
    for line in lines:
        opponend, me = line.strip().split(" ")
        # print("opponend ", opponend)
        # print("me ", me)
        op_num = 0
        me_num = 0
        if opponend == "A":
            op_num = 1
        if opponend == "B":
            op_num = 2
        if opponend == "C":
            op_num = 3

        if me == "X":
            me_num = 1
        if me == "Y":
            me_num = 2
        if me == "Z":
            me_num = 3

        if op_num == me_num:
            my_score += me_num + 3
        elif opponend == "A" and me == "Y":
            my_score += me_num + 6
        elif opponend == "B" and me == "Z":
            my_score += me_num + 6
        elif opponend == "C" and me == "X":
            my_score += me_num + 6
        else:
            my_score += me_num

    return my_score


# part 2
def part_2():
    lines = get_input()

    # A = Rock = 1
    # B = Paper = 2
    # C = Scissor = 3
    #
    # X = lose
    # Y = draw
    # Z = win

    my_score = 0
    for line in lines:
        opponend, result = line.strip().split(" ")

        if result == "X":
            my_score += 0  # lose
            if opponend == "A":
                my_score += 3  # C
            if opponend == "B":
                my_score += 1  # A
            if opponend == "C":
                my_score += 2  # B

        if result == "Y":
            my_score += 3  # draw
            if opponend == "A":
                my_score += 1  # A
            if opponend == "B":
                my_score += 2  # B
            if opponend == "C":
                my_score += 3  # C

        if result == "Z":
            my_score += 6  # win
            if opponend == "A":
                my_score += 2  # B
            if opponend == "B":
                my_score += 3  # C
            if opponend == "C":
                my_score += 1  # A

    return my_score


print("part 1 ", part_1())
print()

print("part 2 ", part_2())
