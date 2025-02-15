class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class CountUnivalueSubtrees:
    def countUnivalueSubtrees(self, root: TreeNode) -> int:
        def post_order(node):
            if not node:
                return 0, True
            
            if not node.left and not node.right:
                return 1, True
            
            left = post_order(node.left)
            right = post_order(node.right)
            
            total = left[0] + right[0]
            if not left[1] or not right[1]:
                return total, False
            
            if node.left != None and node.data != node.left.data:
                return total, False
            if node.right != None and node.data != node.right.data:
                return total, False
            
            return total + 1, True
        
        return post_order(root)[0]

root = TreeNode(5, left = TreeNode(1, left = TreeNode(5), right = TreeNode(5)), right = TreeNode(5, right = TreeNode(5)))
root2 = TreeNode(5, right = TreeNode(5, left = TreeNode(1), right = TreeNode(1)), left = TreeNode(1, left = TreeNode(1), right = TreeNode(1)))

print(CountUnivalueSubtrees().countUnivalueSubtrees(root))
# print()
print(CountUnivalueSubtrees().countUnivalueSubtrees(root2))