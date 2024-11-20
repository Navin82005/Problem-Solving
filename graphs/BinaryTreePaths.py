# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node: TreeNode, tmp):
            if node.right == None and node.left == None:
                result.append(tmp + str(node.val))
                tmp = ""
                return
            tmp += str(node.val) + "->"
            if node.left:
                dfs(node.left, tmp)
            if node.right:
                dfs(node.right, tmp)
        dfs(root, "")
        return result

# Possible test cases
# TreeNode(val= 1, left= TreeNode(val= 2, left= None, right= TreeNode(val= 5, left= None, right= None)), right= TreeNode(val= 3, left= None, right= None))
print(Solution().binaryTreePaths(root=TreeNode(val= 1, left= TreeNode(val= 2, left= None, right= TreeNode(val= 5, left= None, right= None)), right= TreeNode(val= 3, left= None, right= None))))
