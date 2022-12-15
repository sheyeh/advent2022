class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.files = []
        self.subdirectories = []


class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []

    def size(self):
        return sum(file.size for file in self.files) + sum(directory.size() for directory in self.subdirectories)

    def add_file(self, file):
        self.files.append(file)

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)
