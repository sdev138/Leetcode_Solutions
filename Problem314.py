# The TreeNode class is already built in Leetcode
from collections import defaultdict, deque

class Solution:
    # BFS Solution
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        # iterating through the queue
        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]
