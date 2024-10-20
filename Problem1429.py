class FirstUnique:

    def __init__(self, nums: List[int]):
        self.numsList = nums
        self.numsIterations = {}
        self.findIterations(self.numsList)

    def showFirstUnique(self) -> int:
        for num in self.numsList:
            if self.numsIterations[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        if value in self.numsIterations:
            self.numsIterations[value] += 1
        else:
            self.numsIterations[value] = 1

        self.numsList.append(value)
        return

    # determine if the original list has unique and nonunique numbers
    def findIterations(self, numsList: List[int]) -> None:
        for num in numsList:
            if num not in self.numsIterations:
                # if it doesn't exist, set counter to 1
                self.numsIterations[num] = 1
            else:
                self.numsIterations[num] += 1

        return
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value
