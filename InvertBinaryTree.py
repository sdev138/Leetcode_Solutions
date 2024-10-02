class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# the solution class
class Solution:
    # inverting the tree
    def invertTree(self, root: TreeNode):
        # if the root is empty, don't return anything at all
        if not root:
            return None

        # swap the children
        temp = root.right
        root.right = root.left
        root.left = temp

        # recursively calling the function to swap each child
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # printing tree
    def printTree(self, root: TreeNode):
        if not root:
            return None

        # printing the value of the node
        print(root.val)

        self.printTree(root.left)
        self.printTree(root.right)
        return None


# calling the main function
def main():
    print("In the main function")
    # creating some nodes
    # ------- Create some nodes here ----------
    # [2,1,3]
    rootNode = TreeNode(2)
    rootNode.left = TreeNode(1)
    rootNode.right = TreeNode(3)
    solution = Solution()
    rootNode = solution.invertTree(root=rootNode)

    print("Printing the Tree...")
    # printing the binary tree
    solution.printTree(root=rootNode)

main()
