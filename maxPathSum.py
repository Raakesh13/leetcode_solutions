# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        import math
        _max = -math.inf
        _max = self._maxPathSum(root, _max)
        return _max

    def _maxPathSum(self, root, _max):
        if not root:
            return

        if _max < root.val:
            _max = root.val

        if not root.left and not root.right:
            return root.val

        l = root.val + self._maxPathSum(root.left, _max)
        r = root.val + self._maxPathSum(root.right, _max)

        if _max < max(l, r, l+r-root.val):
            _max = max(l, r, l+r-root.val)

        return max(l, r, root.val)

# class Solution(object):
#     mx = float('-inf')

#     def dfs(self, root):
#         if not root:
#             return 0
#         if self.mx < root.val:
#             self.mx = root.val
#         if not root.left and not root.right:
#             return root.val
#         l = root.val + self.dfs(root.left)
#         r = root.val + self.dfs(root.right)
#         if self.mx < max(l, r, l+r-root.val):
#             self.mx = max(l, r, l+r-root.val)
#         return max(l, r, root.val)

#     def maxPathSum(self, root):
#         self.dfs(root)
#         return self.mx


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

ob = Solution()
print(ob.maxPathSum(root))
