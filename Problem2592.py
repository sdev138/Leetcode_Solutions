class Solution:
    def maximumGreatness(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        for num in nums:
            if num > nums[i]:
                i += 1
        return i