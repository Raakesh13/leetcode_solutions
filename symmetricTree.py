# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (root.left and not root.right) or (not root.left and root.right) or (root.left.val != root.right.val):
            return False
        elif root.left.val == root.right.val:
            self.isSymmetric(root.left)
            self.isSymmetric(root.right)
            return True


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
