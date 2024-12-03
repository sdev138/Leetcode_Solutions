class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                # check if the indices are not the same
                if i != hashmap[nums[i]]:
                    # check if it meets the requirements
                    result = i - hashmap[nums[i]]
                    if abs(result) <= k:
                        return True
                    else:
                        hashmap[nums[i]] = i
        return False