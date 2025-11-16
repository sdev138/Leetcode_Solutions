# pascals triangle problem
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        else:
            output = []
            for i in range(numRows):
                output.append([0 * i])

            for i in range(len(output)):
                for j in range(len(output)):
                    if j == 1 or j == len(output[i])-1:
                        output[i][j] = 1
                    else:
                        output[i][j] = output[i-1][j-1] + output[i-1][j]

            return output