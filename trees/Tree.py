class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(node: TreeNode, val: int):
    if not node:
        return TreeNode(val)
    
    if node.val > val:
        node.left = insertNode(node.left, val)
    
    if node.val < val:
        node.right = insertNode(node.right, val)
    
    return node

def inorder(node: TreeNode):
    if node:
        inorder(node.left)
        print(node.val, end= " ")
        inorder(node.right)

def deleteNode(node: TreeNode, val: int):
    
    def get_successor(curr: TreeNode):
        curr = curr.right
        while curr and curr.left:
            curr = curr.left
        return curr

    if not node:
        return node
        
    if node.val > val:
        node.left = deleteNode(node.left, val)
    elif node.val < val:
        node.right = deleteNode(node.right, val)
    else:
        if node.right == None:
            return node.left
        elif node.left == None:
            return node.right
        else:
            tmp = get_successor(node)
            node.val = tmp.val
            node.right = deleteNode(node.right, tmp.val)
    return node

l = [5, 8, 6, 7, 2]

head = None

for i in l:
    head = insertNode(head, i)


head = deleteNode(head, 5)
inorder(head)