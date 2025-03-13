# Knapsack Problem
class Solution:
    def maximumProfit(self, present: list[int], future: list[int], budget: int) -> int:
        dp = [0] * (budget+1)
        for presentValue, futureValue in zip(present, future):
            for j in range(budget, presentValue-1, -1):
                profit = futureValue - presentValue
                dp[j] = max(dp[j], dp[j-presentValue] + (profit))
        return dp[-1]