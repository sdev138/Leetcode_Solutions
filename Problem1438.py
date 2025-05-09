# importing heapq for heap methods
import heapq
class Solution:
    # O(n^2) solution
    # def longestSubarray(self, nums: list[int], limit: int) -> int:
    #     if len(nums) == 1:
    #         return 1
    #     tempList = []
    #     output = 1
    #     for i in range(len(nums)):
    #         tempList.append(nums[i])
    #         for j in range(i+1, len(nums)):
    #             tempList.append(nums[j])
    #             # checking diff
    #             diff = abs(max(tempList) - min(tempList))
    #             if diff <= limit:
    #                 # getting the maximum length
    #                 output = max(output, len(tempList))
    #         tempList.clear()
    #     return output

    # another O(n^2) algorithm
    # def longestSubarray(self, nums: list[int], limit: int) -> int:
    #     if len(nums) == 1:
    #         return 1
    #     i = 0
    #     j = 1
    #     output = 1
    #     tempList = []
    #     tempList.append(nums[0])
    #     while i < len(nums):
    #         if i == len(nums) - 1:
    #             output = max(output, 1)
    #             break
    #         tempList.append(nums[j])
    #         diff = abs(max(tempList) - min(tempList))
    #         if diff <= limit:
    #             output = max(output, len(tempList))
    #         j += 1
    #         if j >= len(nums):
    #             tempList.clear()
    #             i += 1
    #             j = i + 1
    #             if i < len(nums):
    #                 tempList.append(nums[i])

    #     return output

    # using two heaps
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_heap = []
        min_heap = []

        left = 0
        max_length = 0

        for right in range(len(nums)):
            # pushing both indexes to different heaps
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (-nums[right], right))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            max_length = max(max_length, right - left + 1)

        return max_length

# main executable for testing
def main():
    solution = Solution()
    output = solution.longestSubarray(nums=[8,5,6,2,3,9], limit=4)
    print("Value of solution: ", output)
    return

main()
