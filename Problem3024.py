class Solution:
    def triangleType(self, nums: list[int]) -> str:
        # if all sides are equal: equilateral 
        # if two sides equal: isosceles
        # if all different sides: scalene
        if not nums or len(nums) != 3:
            return "none"
        elif nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"

        numsMap = {}
        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                numsMap[num] += 1
        
        for key, value in numsMap.items():
            if value == 2:
                return "isosceles"
            elif value == 3:
                return "equilateral"
        return "scalene"