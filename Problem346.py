class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.window.pop(0)
        self.window.append(val)
        output = 0
        for num in self.window:
            output += num
        output /= len(self.window)

        return output
