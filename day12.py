# day 12

import sys
import networkx as nx  # type: ignore
from rich.progress import track

# oh oh 😱 global 🤯
global heights


def get_input():
    with open("2022/day12 input.txt") as f:
        return [x.strip() for x in f.readlines()]


def build_graph(input):
    global heights
    line = input.pop(0)
    input.insert(0, line)
    row_length = len(line)
    max_num = row_length * row_length

    heights = []
    start_positions = []

    graph = nx.DiGraph()
    first, last, num = 0, 0, 0
    for line in input:
        start_positions.append(num)
        for char in line:
            if char == "S":
                value = ord("a")
                first = num
            elif char == "E":
                value = ord("z")
                last = num
            else:
                value = ord(char)

            heights.append(value)

            x_pos = num % row_length
            if num - row_length >= 0:
                graph.add_weighted_edges_from([(num - row_length, num, int(value))])
            if x_pos - 1 >= 0:
                graph.add_weighted_edges_from([(num - 1, num, int(value))])
            if x_pos < row_length - 1:
                graph.add_weighted_edges_from([(num + 1, num, int(value))])
            if num + row_length < max_num - 1:
                graph.add_weighted_edges_from([(num + row_length, num, int(value))])
            num += 1

    return graph, first, last, num, start_positions


def weight(u, v, w):
    global heights
    if heights[v] - heights[u] <= 1:
        return 1
    else:
        return sys.maxsize


# part 1
def part_1():
    steps = 0
    graph, first, last, number_nodes, _ = build_graph(get_input())
    path = nx.dijkstra_path(graph, first, last, weight)
    steps = len(path) - 1
    return steps


# part 2
def part_2():
    steps = 0
    """
    'b' occurs only in the second column -> so we consider only the a's in the first column
    """
    graph, first, last, number_nodes, start_positions = build_graph(get_input())

    results = []
    for start in track(start_positions):
        if heights[start] == ord("a"):
            path = nx.dijkstra_path(graph, start, last, weight)
            results.append(len(path) - 1)
        else:
            pass

    steps = min(results)
    return steps


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
