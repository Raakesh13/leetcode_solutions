class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root):
        num = 0
        return self.sumnumber(root, num)

    def sumnumber(self, root, num):
        num = num*10 + root.val
        if root.left == None and root.right == None:
            return num
        else:
            return self.sumnumber(root.left, num) + \
                self.sumnumber(root.right, num)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

ob = Solution()
print(ob.sumNumbers(root))
