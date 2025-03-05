# in order traversal of a binary tree
# Note: Optional and List are Leetcode specific classes
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is not None:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)

def main():
    # create your nodes
    # perform inorder traversal
    solution = Solution()
    # feel free to run your tests using the main function below
    return