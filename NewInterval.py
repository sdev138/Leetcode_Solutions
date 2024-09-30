# credit for this algorithm goes to Neetcode
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        # iterating through the list
        for i in range(len(intervals)):
            # if the last element of a new interval is less than the beginning element of any interval
            if newInterval[1] < intervals[i][0]:
                # if this is the case we add the element and return the remaining intervals
                res.append(newInterval)
                return res + intervals[i:]
            # if the beginning element is greater than the last element of any interval, we simply add the iterated interval to the result list
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(
                    newInterval[1], intervals[i][1])]
        res.append(newInterval)
        # returning the result
        return res


def main():
    input = [[1, 2], [5, 8], [10, 15]]
    target = [2, 9]
    solution = Solution()
    result = solution.insert(input, target)
    print("Value of result: ", result)


main()
