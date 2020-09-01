class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            nodeList = []
            self.inorder(root, nodeList)
            copy_nodeList = [i for i in nodeList]
            copy_nodeList.sort()
            print(copy_nodeList, nodeList)
            return copy_nodeList == nodeList

    def inorder(self, root, nodeList):
        if root:
            self.inorder(root.left, nodeList)
            nodeList.append(root.val)
            self.inorder(root.right, nodeList)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
ob = Solution()
print(ob.isValidBST(root))
