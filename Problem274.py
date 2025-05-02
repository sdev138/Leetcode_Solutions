class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        i = 0
        while i < len(citations) and citations[len(citations) - 1 - i] > i:
            i += 1

        return i
            
# For testing purposes only
def main():
    test = [3, 0, 6, 1, 5]
    solution = Solution()
    hValue = solution.hIndex(citations=test)
    print("hValue: ", hValue)

main()