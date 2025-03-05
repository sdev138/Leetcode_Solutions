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


def printHelloWorld():
    print("Hello World")
    print("Testing some helix config changes as well as changes to zsh")
    return

def main():
    print("In the main function")
    pass
    print("After the pass keyword")


main()
