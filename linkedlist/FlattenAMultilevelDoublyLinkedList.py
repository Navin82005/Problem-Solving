from typing import Optional, Self


class Node:
    def __init__(self, val, prev: Self, next: Self, child: Self):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class FlattenAMultilevelDoublyLinkedList:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        
        def dfs(node, prv):
            if not node:
                return prv
            
            if node.cild:
                cur = node
                prv = dfs(node.child, node)
                cur.next = prv
                # cur.prev = 
                cur.child = None
            
            if node.next:
                prv = dfs(node.next, node)

        return head

root = Node(1, )

print(FlattenAMultilevelDoublyLinkedList().flatten(root))