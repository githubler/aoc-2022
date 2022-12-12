# day 11

from rich.console import Console
from rich.text import Text
from rich.progress import track


def get_input():
    monkeys = []
    """
    # Test Data
    items = [79, 98]
    operation = ["*", 19]
    test = [23, 2, 3]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [54, 65, 75, 74]
    operation = ["+", 6]
    test = [19, 2, 0]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [79, 60, 97]
    operation = ["*", "old"]
    test = [13, 1, 3]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [74]
    operation = ["+", 3]
    test = [17, 0, 1]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)
    """

    # """
    items = [91, 66]
    operation = ["*", 13]
    test = [19, 6, 2]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [78, 97, 59]
    operation = ["+", 7]
    test = [5, 0, 3]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [57, 59, 97, 84, 72, 83, 56, 76]
    operation = ["+", 6]
    test = [11, 5, 7]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [81, 78, 70, 58, 84]
    operation = ["+", 5]
    test = [17, 6, 0]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [60]
    operation = ["+", 8]
    test = [7, 1, 3]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [57, 69, 63, 75, 62, 77, 72]
    operation = ["*", 5]
    test = [13, 7, 4]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [73, 66, 86, 79, 98, 87]
    operation = ["*", "old"]
    test = [3, 5, 2]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)

    items = [95, 89, 63, 67]
    operation = ["+", 2]
    test = [2, 1, 4]
    monkey = Monkey(items, operation, test)
    monkeys.append(monkey)
    # """

    return monkeys


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.monkeys = []
        self.num_inspect = 0

    def set_monkeys(self, monkeys):
        self.monkeys = monkeys

    def receive_item(self, item):
        self.items.append(item)

    def inspect(self, decrease=0):
        # items = (self.items).copy()
        for item in self.items:
            num = 0
            self.num_inspect += 1
            if self.operation[1] == "old":
                num = item
            else:
                num = self.operation[1]

            if self.operation[0] == "*":
                item *= num
            else:
                item += num

            if decrease == 0:
                item //= 3
            else:
                item %= 9699690

            if not (item % self.test[0]):
                self.monkeys[self.test[1]].receive_item(item)
            else:
                self.monkeys[self.test[2]].receive_item(item)

        self.items = []  # clear()


# part 1
def part_1():
    monkey_business = 0

    monkeys = get_input()

    for monkey in monkeys:
        monkey.set_monkeys(monkeys)

    console = Console()
    text = Text()
    for round in track(range(1, 21)):
        for monkey in monkeys:
            monkey.inspect()

    total_numbers = []
    for i, monkey in enumerate(monkeys):
        total_numbers.append(monkey.num_inspect)
        text = "Monkey " + str(i) + " inspected items " + str(monkey.num_inspect) + " times."
        console.print(text)
    print()

    total_numbers.sort()
    monkey_business = total_numbers[-1] * total_numbers[-2]

    return monkey_business


# part 2
def part_2():
    monkey_business = 0

    monkeys = get_input()

    for monkey in monkeys:
        monkey.set_monkeys(monkeys)

    console = Console()
    text = Text()
    for round in track(range(1, 10001)):
        for monkey in monkeys:
            monkey.inspect(1)

    total_numbers = []
    for i, monkey in enumerate(monkeys):
        total_numbers.append(monkey.num_inspect)
        text = "Monkey " + str(i) + " inspected items " + str(monkey.num_inspect) + " times."
        console.print(text)
    print()

    total_numbers.sort()
    monkey_business = total_numbers[-1] * total_numbers[-2]

    return monkey_business


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
