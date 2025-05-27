# Each element will only appear at most TWICE!!!
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        seen = set()
        
        for num in nums:
            if num in seen:
                dup.append(num)
            else:
                seen.add(num)
        
        return dup

solution = Solution()
print(solution.findDuplicates([1, 1, 2]))