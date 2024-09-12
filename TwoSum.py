# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    # initializing the empty constructor here
    def __init__(self) -> None:
        pass
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapIndex = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in mapIndex:
                # adding the number and index to dict
                mapIndex[nums[i]] = i
            # if their is a match
            else:
                # adding the indices to the solution list
                return [mapIndex[diff], i]
        return []

# main function to call the solution
def main():
    solution = Solution()
    returnedIndices = solution.twoSum([3, 4, 1, 6, 5, 9], 15)
    print("Here are the following indices: ", returnedIndices)

main()
