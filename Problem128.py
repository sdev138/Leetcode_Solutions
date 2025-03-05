class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        nums = sorted(nums)
        longestSubSeq = 1
        subSeq = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1] and nums[i] != nums[i-1]:
                subSeq += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                subSeq = 1
            longestSubSeq = max(longestSubSeq, subSeq)
        print(longestSubSeq)
        return longestSubSeq
