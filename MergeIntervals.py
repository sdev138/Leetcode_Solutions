# The following is a solution to problem 56 "Merge Intervals"
# Incomplete

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        print("In the merge function")
        start = 0
        end = 0
        ans = []
        for interval in intervals:
            # iterating through the interval 
            startCurrent = interval[0]
            endCurrent = interval[-1]
            if endCurrent <= end:
                end = endCurrent

def main():
    print("In the main function")
    pass

main()