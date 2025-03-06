class Solution:
    # O(n) solution
    def findPeakElement(self, nums: list[int]) -> int:
        max_element = max(nums)

        for i in range(len(nums)):
            if nums[i] == max_element:
                return i
        
        return 0

    # better O(n) solution as a peak is simply greater than its neighbors not necessarily the greatest
    def returnAPeak(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        
        return len(nums) - 1

    # binary search solution
    def binarySearchPeak(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        # binary search
        
        return 0
