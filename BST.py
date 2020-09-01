class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        if self.leftChild:
            return True
        else:
            return False

    def hasRight(self):
        if self.rightChild:
            return True
        else:
            return False

    def _insert(self, data):
        if self.val < data:
            self.rightChild = Node(data)
        else:
            self.leftChild = Node(data)

    def _traverse(self):
        if self:
            if self.leftChild:
                self.leftChild._traverse()
            print(self.val)
            if self.rightChild:
                self.rightChild._traverse()


class BST():
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        elif val < self.root.val:
            if self.root.leftChild:
                self.root._insert(val)
        else:
            self.root.leftChild = Node(val)

        # else:
        #     if self.root.rightChild:
        #         self.root._insert(val)
        #     else:
        #         self.rightChild = Node(val)

    def traverse(self):
        self.root._traverse()


ob = BST()
ob.insert(9)
# print(ob.root.val)
ob.insert(5)
# print(ob.root.val)
ob.insert(10)
ob.insert(1)
ob.insert(16)
ob.insert(3)
ob.insert(12)
ob.insert(11)
ob.insert(7)

# print(ob.root.val)
ob.traverse()
# print(ob.root.rightChild.val)
