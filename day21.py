# day 21

from icecream import ic
from rich.progress import Progress

from collections import deque


def get_input():
    with open("2022/day21 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def evaluate(nodes, name):
    task = nodes[name]
    if len(task) == 1:
        return task[0]
    else:
        expr_a = evaluate(nodes, task[0])
        expr_b = evaluate(nodes, task[2])
        result = eval(f"{expr_a} {task[1]} {expr_b}")
        return result


def evaluate_2(nodes, name):
    task = nodes[name]
    if len(task) == 1:
        return task[0]
    else:
        expr_a = evaluate_2(nodes, task[0])
        expr_b = evaluate_2(nodes, task[2])
        if name == "root":
            return expr_a, expr_b
        else:
            result = eval(f"{expr_a} {task[1]} {expr_b}")
            return result


# part 1
def part_1():
    num = 0

    nodes = {}
    for line in get_input():
        input = line.split()
        name = input[0].split(":")[0]
        task = line.split(":")[1]
        nodes.update({name: list(task.split())})

    num = evaluate(nodes, "root")

    return num


# part 2
def part_2():
    num = 0

    nodes = {}
    for line in get_input():
        input = line.split()
        name = input[0].split(":")[0]
        task = line.split(":")[1]
        nodes.update({name: list(task.split())})

    root_task = nodes["root"]
    root_task[1] = "=="
    nodes.update({"root": root_task})
    # try & error :-(
    nodes.update({"humn": ["3032671800000"]})

    with Progress() as progress:
        task = progress.add_task("Working ...", total=350)

        num = 3032671800000
        while True:
            a, b = evaluate_2(nodes, "root")
            if a == b:
                break
            num += 1
            nodes.update({"humn": [str(num)]})
            progress.update(task, advance=1)

    return num


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
