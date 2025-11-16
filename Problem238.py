from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, output = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        left[0] = 1
        right[-1] = 1

        for i in range(1, len(left)):
            left[i] = nums[i-1] * left[i-1]
        
        for i in reversed(range(len(right) - 1)):
            right[i] = nums[i+1] * right[i+1]

        for i in range(len(nums)):
            output[i] = left[i] * right[i] 

        return output