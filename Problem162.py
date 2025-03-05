class Solution:
    # O(n) solution
    def findPeakElement(self, nums: list[int]) -> int:
        max_element = max(nums)

        for i in range(len(nums)):
            if nums[i] == max_element:
                return i
        
        return 0
