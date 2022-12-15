import re

from files import File, Directory

FILE_MATCH = re.compile("(\\d*) (.*)")
path: list[Directory] = []
directories = []
directory: [None, Directory] = None
with open('day7.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line == "$ cd ..":
            path.pop()
            directory = path[len(path) - 1]
        elif line.startswith("$ cd "):
            name = line[5:]
            _dir = Directory(name)
            path.append(_dir)
            directories.append(_dir)
            if directory:
                directory.add_subdirectory(_dir)
            directory = _dir
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            continue
        else:
            p = FILE_MATCH.match(line)
            file_size = int(p.group(1))
            file_name = p.group(2)
            file = File(file_name, file_size)
            directory.add_file(file)


sizes = [directory.size() for directory in directories]
result = sum(size for size in sizes if size < 100000)
print(result)
