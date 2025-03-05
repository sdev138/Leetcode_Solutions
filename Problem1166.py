from collections import defaultdict


class FileSystem:
    # initializing the paths as a defaultdict
    def __init__(self):
        self.paths = defaultdict()

    # creating the path using linux notation
    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or len(path) == 0 or path in self.paths:
            return False

        parent_path = path[: path.rfind("/")]
        if len(parent_path) > 1 and parent_path not in self.paths:
            return False

        self.paths[path] = value
        return True

    # getting the path from the defaultdict
    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
