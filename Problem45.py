class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJumps = 0
        for i in range(len(nums)):
            currentJump = nums[i]

            if i == len(nums) - 1:
                return totalJumps
            elif i + currentJump >= len(nums) - 1:
                return totalJumps + 1

            maxElement = 0
            for j in range(i + 1, i + currentJump):
                # find the biggest element and replace i index
                if nums[j] > maxElement:
                    maxElement = nums[j]
                    i = j - 1

            totalJumps += 1
