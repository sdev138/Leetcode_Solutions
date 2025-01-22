import collections

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairsMap = collections.defaultdict(list)
        counter = 0
        for i in range(len(nums)):
            complement = k - nums[i]
            if complement in pairsMap and len(pairsMap) > 0:
                # remove complement from the map
                if len(pairsMap[complement]) == 1:
                    del pairsMap[complement]
                else:
                    pairsMap[complement].pop()

                counter += 1
            else:
                # add current element to the map
                pairsMap[nums[i]].append(i)

        return counter