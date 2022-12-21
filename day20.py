# day 20

from rich.progress import track

from collections import deque


def get_input():
    with open("2022/day20 input.txt") as f:
        return [x.strip() for x in f.readlines()]


# part 1
def part_1():
    sum = 0
    sequence = list()
    mixing = deque()

    index_0 = 0
    for i, num in enumerate(get_input()):
        num = int(num)
        sequence.append(num)
        mixing.append({i: num})
        if num == 0:
            index_0 = i

    for i in track(range(len(sequence))):
        index = mixing.index({i: sequence[i]})
        new_index = (index + sequence[i]) % (len(sequence) - 1)
        del mixing[index]
        if new_index == 0:
            mixing.append({i: sequence[i]})
        else:
            mixing.insert(new_index, {i: sequence[i]})

    index = mixing.index({index_0: sequence[index_0]})
    for _ in range(3):
        index += 1000
        index %= len(sequence)
        test = mixing[index]
        sum += list(mixing[index].values())[0]

    return sum


# part 2
def part_2():
    sum = 0
    sequence = list()
    mixing = deque()

    index_0 = 0
    for i, num in enumerate(get_input()):
        num = int(num) * 811589153
        sequence.append(num)
        mixing.append({i: num})
        if num == 0:
            index_0 = i

    for _ in range(10):
        for i in track(range(len(sequence))):
            index = mixing.index({i: sequence[i]})
            new_index = (index + sequence[i]) % (len(sequence) - 1)
            del mixing[index]
            if new_index == 0:
                mixing.append({i: sequence[i]})
            else:
                mixing.insert(new_index, {i: sequence[i]})

    index = mixing.index({index_0: sequence[index_0]})
    for _ in range(3):
        index += 1000
        index %= len(sequence)
        test = mixing[index]
        sum += list(mixing[index].values())[0]

    return sum


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
