from typing import List;

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        maxJump = 0
        for jump in range(len(nums)):
            if nums[jump] > maxJump:
                maxJump = nums[jump]
            
            # checking if its within bounds 
            if maxJump <= 0 and jump < len(nums) - 1:
                return False
            
            # for iteration
            maxJump -= 1
        return True

def main():
    testArray = [2, 0, 0]
    solution = Solution()
    jumpSolution = solution.canJump(testArray)
    if jumpSolution:
        print("True: Can reach last index")
    else:
        print("True: Can reach last index")
