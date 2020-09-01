class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _preorder(self):
        if self:
            print(self.data, end=" ")
            if self.left:
                self.left._preorder()
            if self.right:
                self.right._preorder()

    def _inorder(self):
        if self:

            if self.left:
                self.left._preorder()
            print(self.data, end=" ")
            if self.right:
                self.right._preorder()

    def _postorder(self):
        if self:

            if self.left:
                self.left._preorder()

            if self.right:
                self.right._preorder()

            print(self.data, end=" ")

    def _search(self, val, current):
        if current.data == val:
            return True

        elif current.data > val:
            if current.left:
                return self._search(val, current.left)
            else:
                return False

        elif current.data < val:
            if current.right:
                return self._search(val, current.right)
            else:
                return False

    def _insert(self, data):
        if data < self.data:
            if self.left:
                self.left._insert(data)
            else:
                self.left = Node(data)

        elif data > self.data:
            if self.right:
                self.right._insert(data)
            else:
                self.right = Node(data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root._insert(data)

    def preorder_dfs(self):
        self.root._preorder()

    def postorder_dfs(self):
        self.root._postorder()

    def inorder_dfs(self):
        self.root._inorder()

    def search(self, val):
        if self.root:
            return self.root._search(val, self.root)
        else:
            return "Empty tree"


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


ob.postorder_dfs()
