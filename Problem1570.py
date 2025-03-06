class SparseVector:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.length = len(nums)

    def dotProduct(self, vect: 'SparseVector') -> int:
        if len(self.nums) != vect.length:
            return -1
        
        output = 0
        for num1, num2 in zip(self.nums, vect):
            output += num1 * num2

        return output