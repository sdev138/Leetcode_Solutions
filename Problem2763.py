class Solution:
    def sumImbalanceNumbers(self, A: list[int]) -> int:
        n = len(A)
        res = 0
        for i in range(n):
            s = set()
            cur = -1
            for j in range(i, n):
                cur += 0 if A[j] in s else 1 - (A[j] + 1 in s) - (A[j] - 1 in s)
                s.add(A[j])
                res += cur
            return res
