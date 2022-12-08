# day 08


def get_input():
    with open("2022/day08 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def build_grid():
    swarm = []
    for line in get_input():
        swarm.append([int(x) for x in line])
    return swarm


def is_visible_x(x, y, grid) -> bool:
    visible_left = True
    visible_right = True

    # search left side
    for _x in range(x):
        origin = grid[y][x]
        test = grid[y][_x]
        if grid[y][_x] >= grid[y][x]:
            visible_left = False
            break

    # search right side
    for _x in range(x + 1, len(grid[0])):
        origin = grid[y][x]
        test = grid[y][_x]
        if grid[y][_x] >= grid[y][x]:
            visible_right = False
            break

    return visible_left or visible_right


def is_visible_y(x, y, grid) -> bool:
    visible_up = True
    visible_down = True

    # search up
    for _y in range(y):
        origin = grid[y][x]
        test = grid[_y][x]
        if grid[_y][x] >= grid[y][x]:
            visible_up = False
            break

    # search down
    for _y in range(y + 1, len(grid)):
        origin = grid[y][x]
        test = grid[_y][x]
        if grid[_y][x] >= grid[y][x]:
            visible_down = False
            break

    return visible_up or visible_down


def calc_score_x(x, y, grid) -> int:
    score_left = 0
    score_right = 0

    # search left side
    for _x in range(x - 1, -1, -1):
        origin = grid[y][x]
        test = grid[y][_x]
        if grid[y][_x] >= grid[y][x]:
            score_left += 1
            break
        else:
            score_left += 1

    # search right side
    for _x in range(x + 1, len(grid[0])):
        origin = grid[y][x]
        test = grid[y][_x]
        if grid[y][_x] >= grid[y][x]:
            score_right += 1
            break
        else:
            score_right += 1

    if score_left == 0:
        return score_right
    elif score_right == 0:
        return score_left
    else:
        return score_left * score_right


def calc_score_y(x, y, grid) -> int:
    score_up = 0
    score_down = 0

    # search up
    for _y in range(y - 1, -1, -1):
        origin = grid[y][x]
        test = grid[_y][x]
        if grid[_y][x] >= grid[y][x]:
            score_up += 1
            break
        else:
            score_up += 1

    # search down
    for _y in range(y + 1, len(grid)):
        origin = grid[y][x]
        test = grid[_y][x]
        if grid[_y][x] >= grid[y][x]:
            score_down += 1
            break
        else:
            score_down += 1

    if score_up == 0:
        return score_down
    elif score_down == 0:
        return score_up
    else:
        return score_up * score_down


# part 1
def part_1():
    grid = build_grid()

    num_visible_trees = len(grid[0]) * 2 + (len(grid) - 2) * 2

    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            visible_x = is_visible_x(x, y, grid)
            visible_y = is_visible_y(x, y, grid)
            if visible_x or visible_y:
                num_visible_trees += 1

    return num_visible_trees


# part 2
def part_2():
    grid = build_grid()

    scenic_score = 0
    score = 0

    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):

            num = grid[y][x]
            score_x = calc_score_x(x, y, grid)
            score_y = calc_score_y(x, y, grid)
            score = score_x * score_y

            if score > scenic_score:
                scenic_score = score

    return scenic_score


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
