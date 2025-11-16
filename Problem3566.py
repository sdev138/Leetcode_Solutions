from typing import List
import math 

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        totalProduct = math.prod(nums)
        if totalProduct == target**2:
            return True
        else:
            return False
