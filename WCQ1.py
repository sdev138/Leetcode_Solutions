class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0 

        output = 0
        if n > k:
            diff = abs(k - n)
            output += (diff*k) 

        if m > k:
            diff = abs(k - m)
            output += (diff*k)

        return output