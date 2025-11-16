class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not returns anything, modify nums in-place instead
        """
        # find each permutation, calculate the lexographic order, put them into an array
        # based on lexographic order, then find the current array and return the next one
        if not nums:
            return 
        else:
            i = len(nums) - 2
            while i >= 0 and nums[i+1] <= nums[i]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while nums[j] <= nums[i]:
                    j -= 1
                self.swap(nums, i, j)
            self.reverse(nums, i + 1)
        print(nums)
        return 

    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
        return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return

                
solution = Solution()
solution.nextPermutation(nums=[1,2,3])