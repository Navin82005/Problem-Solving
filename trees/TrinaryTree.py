class TrinaryTreeNode:
    def __init__(self, val: int, left = None, mid = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.mid = mid

class TrinaryTree:
    def __init__(self, **keywords):
        self.head = None
        if "head" in keywords:
            self.head = keywords["head"]
        if "data" in keywords:
            for i in keywords["data"]:
                self.insertVal(i)
    
    def insertVal(self, val: int):
        if self.head == None:
            self.head = TrinaryTreeNode(val)
            return
        self._insert_recursive(self.head, val)
    
    def _insert_recursive(self, node: TrinaryTreeNode, val: int):
        if node.left == None:
            node.left = TrinaryTreeNode(val)
        elif node.mid == None:
            node.mid = TrinaryTreeNode(val)
        elif node.right == None:
            node.right = TrinaryTreeNode(val)
        else:
            if node.left != None:
                self._insert_recursive(node.left, val)
            elif node.mid != None:
                self._insert_recursive(node.mid, val)
            elif node.right != None:
                self._insert_recursive(node.right, val)
    
    def postOrder(self):
        self._postOrder(self.head)
    
    def _postOrder(self, node: TrinaryTreeNode):
        if not node:
            return
        self._postOrder(node.left)
        self._postOrder(node.mid)
        self._postOrder(node.right)
        print(print(node.val))

l = [1, 2, 3, 4, 6, 7, 8]
head = TrinaryTree(data=l)

head.postOrder()