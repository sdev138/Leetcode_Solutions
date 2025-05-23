class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in complementMap:
                complementMap[nums[i]] = i
            else:
                return [min(complementMap[complement], i), max(complementMap[complement], i)]