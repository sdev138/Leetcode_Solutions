# The following is a solution to problem 56 "Merge Intervals"
# Incomplete


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        print("In the merge function")
        start = 0
        end = 0
        for interval in intervals:
            # iterating through the interval
            startCurrent = interval[0]
            endCurrent = interval[-1]
            if endCurrent <= end:
                end = endCurrent
                start = startCurrent
        return intervals


# calling the main function
def main():
    solution = Solution()
    intervals = [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8]]
    output = solution.merge(intervals)
    print(output)

main()
