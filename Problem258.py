class Solution:
    # Keeps adding the numbers until the result is a single digit number
    def addDigits(self, num: int) -> int:
        if num // 10 == 0:
            return num
        result = 0
        while num != 0:
            digit = num % 10
            result += digit

            num = num // 10

        return self.addDigits(result)


def main():
    valueParam = 38
    # valueParam = 122
    solution = Solution()
    output = solution.addDigits(valueParam)
    print("Value of output: ", output)


main()
