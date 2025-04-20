class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minNum = min(nums)
        for num in nums:
            if num % minNum:
                return 1
        return (nums.count(minNum) + 1) // 2
