class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root):
        wrongVals = []
        self.dfs(root, wrongVals, TreeNode(float("-inf")))
        wrongVals[0].val, wrongVals[1].val = wrongVals[1].val, wrongVals[0].val

    def dfs(self, root, wrongVals, lastNode):
        if root.left:
            lastNode = self.dfs(root.left, wrongVals, lastNode)

        if lastNode.val > root.val:
            if wrongVals:
                wrongVals[1] = root

            else:
                wrongVals += [lastNode, root]

        lastNode = root

        if root.right:
            lastNode = self.dfs(root.right, wrongVals, lastNode)

        return lastNode


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
ob = Solution()
ob.recoverTree(root)
print(root.val)
