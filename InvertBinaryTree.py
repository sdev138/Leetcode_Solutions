class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if the root is empty, don't return anything at all
        if not root:
            return None

        # swap the children
        temp = root.right
        root.right = root.left 
        root.left = temp

        # recursively calling the function to swap each child
        self.invertTree(self, root.left)
        self.invertTree(self, root.right)
        return root

def main():
    # creating some nodes
    # ------- Create some nodes here ----------
    rootNode = TreeNode()
    solution = Solution()
    solution.invertTree(rootNode)