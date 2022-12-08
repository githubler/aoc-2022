# day 07


def get_input():
    with open("2022/day07 input.txt") as f:
        return [x.strip() for x in f.readlines()]


class File:
    def __init__(self, name, size):
        self.size = int(size)
        self.name = name


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.directories = []
        self.files = []

    def add_directory(self, directory):
        self.directories.append(directory)

    def add_file(self, file):
        self.files.append(file)

    def get_dir(self, directory):
        for dir in self.directories:
            if dir.get_name() == directory:
                return dir

    def get_parentdir(self):
        return self.parent

    def is_root(self):
        return "/" == self.name

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return str(self)

    def get_size(self, small_dirs=None) -> int:
        size = 0
        for file in self.files:
            size += file.size

        for dir in self.directories:
            size += dir.get_size(small_dirs)

        if size <= 100000 and small_dirs != None:
            small_dirs.append(self)

        return size

    def get_dirs_delete(self, dirs, value) -> int:
        size = 0
        for file in self.files:
            size += file.size

        for dir in self.directories:
            size += dir.get_dirs_delete(dirs, value)

        if size >= value and dirs != None:
            dirs.append(size)

        return size


def build_filesystem():
    root = Directory("/")
    current_dir = root

    for line in get_input():
        if line[0] == "$":
            if line != "$ ls":
                _, _, dir_name = line.split()
                if dir_name == "/":
                    current_dir = root
                elif dir_name == "..":
                    current_dir = current_dir.get_parentdir()
                else:
                    current_dir = current_dir.get_dir(dir_name)
        else:
            if line.startswith("dir"):
                _, name = line.split()
                new_dir = Directory(name, current_dir)
                current_dir.add_directory(new_dir)
            else:
                size, name = line.split()
                file = File(name, size)
                current_dir.add_file(file)

    return root


# part 1
def part_1():
    size = 0
    root = build_filesystem()

    small_dirs = []
    root.get_size(small_dirs)

    for dir in small_dirs:
        size += dir.get_size()

    return size


# part 2
def part_2():
    size = 0
    dirs = []

    total_disk_space = 70000000
    min_unused_space = 30000000

    root = build_filesystem()
    size = root.get_size()

    size_to_delete = min_unused_space - (total_disk_space - size)
    root.get_dirs_delete(dirs, size_to_delete)

    return min(dirs)


print()
print("part 1 ", part_1())
print()
print("part 2 ", part_2())
print()
