class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        else:
            queue = [root]
            while queue:
                l = len(queue)
                for i in range(l-1):
                    current = queue.pop()
                    if queue:
                        current.next = queue[-1]

                    if current.left:
                        queue.insert(0, current.left)

                    if current.right:
                        queue.insert(0, current.right)

        return root


ob = Node(1)
ob.left = Node(2)
ob.left.left = Node(4)
ob.left.right = Node(5)
ob.right = Node(3)
ob.right.right = Node(7)

ob2 = Solution()
ob2.connect(ob)
