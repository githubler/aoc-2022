# day 10

from rich.console import Console
from rich.text import Text


def get_input():
    with open("2022/day10 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def check_cycle(cycle) -> bool:
    cycle -= 20
    if cycle == 0 or not (cycle % 40):
        return True
    else:
        return False


def signal_strength(cycle, value) -> int:
    return cycle * value


# part 1
def part_1():
    total_strength = 0

    cycle = 1
    register = 1

    for line in get_input():
        try:
            cmd, num = line.split()
        except ValueError:
            cmd = "noop"

        if cmd == "noop":
            check = check_cycle(cycle)
            if check:
                total_strength += signal_strength(cycle, register)
            cycle += 1
        else:
            check = check_cycle(cycle)
            if check:
                total_strength += signal_strength(cycle, register)
            cycle += 1
            check = check_cycle(cycle)
            if check:
                total_strength += signal_strength(cycle, register)
            cycle += 1
            register += int(num)

    return total_strength


def draw_pixel(crt_pos, register) -> bool:
    sprite_pos = [register - 1, register, register + 1]
    if crt_pos in sprite_pos:
        return True
    else:
        return False


def next_position(cycle, row, pos):
    if not (cycle == 1) and not ((cycle - 1) % 40):
        return (row + 1), 0
    else:
        return row, (pos + 1)


# part 2
def part_2():
    screen = [[" " for _ in range(40)] for _ in range(6)]

    cycle = 1
    register = 1
    row = 0
    pos = -1

    for line in get_input():
        try:
            cmd, num = line.split()
        except ValueError:
            cmd = "noop"

        if cmd == "noop":
            row, pos = next_position(cycle, row, pos)
            if draw_pixel(pos, register):
                screen[row][pos] = "#"
            cycle += 1
        else:
            row, pos = next_position(cycle, row, pos)
            if draw_pixel(pos, register):
                screen[row][pos] = "#"
            cycle += 1

            row, pos = next_position(cycle, row, pos)
            if draw_pixel(pos, register):
                screen[row][pos] = "#"
            cycle += 1

            register += int(num)

    return screen


print()
print("part 1 ", part_1())
print()
print("part 2 ")
screen = part_2()
console = Console()
text = Text()
for y in range(6):
    for x in range(40):
        text.append(screen[y][x])
    text.append("\n")
text.stylize("red")
console.print(text)

print()
