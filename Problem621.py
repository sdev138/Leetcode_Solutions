class Solution:
    def leastInterval(self, tasks: List[int], n: int) -> int:
        if n == 0 or n == 1:
            return len(tasks)