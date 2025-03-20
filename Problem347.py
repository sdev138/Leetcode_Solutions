class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        frequentMap = {}

        for i in nums:
            if i not in frequentMap:
                frequentMap[i] = 1
            else:
                frequentMap[i] += 1

        sortedFrequentMap = dict(
            sorted(frequentMap.items(), key=lambda item: item[1], reverse=True)
        )

        output = []
        kCounter = 0
        # iterating through the map
        for key, value in sortedFrequentMap.items():
            if kCounter == k:
                break
            else:
                output.append(key)
                kCounter += 1
        return output
