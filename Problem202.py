# iterative solution (Faster than 100% runtime, 0% better in memory)
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 2:
            return False
        else:
            storage = [n]
            output = 0
            for i in str(n):
                output += int(i) ** 2

            while True:
                if output == 1:
                    return True
                elif output == 2 or output in storage:
                    return False
                else:
                    storage.append(output)
                    temp = 0
                    for i in str(output):
                        temp += int(i) ** 2
                    output = temp


# Recursive Solution (Faster than 40% runtime, better than 100% memory)
class SolutionRecursive:
    def isHappy(self, n: int) -> bool:
        if n == 0 or n == 2:
            return False
        if n == 1:
            return True

        storage = []

        return self.checkHappy(n, storage)

    def checkHappy(self, num: int, storage: list[int]) -> bool:
        if num in storage or num == 0 or num == 2:
            return False
        elif num == 1:
            return True
        else:
            output = 0
            storage.append(num)
            for i in str(num):
                output += int(i) ** 2

            return self.checkHappy(output, storage)

def main():
    print("Welcome to Problem 202, The Happy Number Checker!")
    # feel free to change the number here
    num = 19
    iterativeSolution = Solution()
    recursiveSolution = SolutionRecursive()

    print("Current Number to check: ", num)

    if iterativeSolution.isHappy(num):
        print("The number is happy")
    else:
        print("The number is not happy")

    if recursiveSolution.isHappy(num):
        print("The number is happy")
    else:
        print("The number is not happy")

main()