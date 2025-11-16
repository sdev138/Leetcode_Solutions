"""
TreeNode class for testing
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
The Solution class is the only real chunk of code that matters
"""
class Solution:
    value = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        Solution.value = 0
        if not root:
            return 0

        self.dfs(root=root)
        return Solution.value

    def dfs(self, root):
        if not root:
            return
        else:
            Solution.value += 1
        # going left and right searching for nodes
        self.dfs(root.left)
        self.dfs(root.right)
        return
