from collections import deque

class LevelOrder:
    def levelOrder(self, root: list):
        q = deque([root])
        res = []
        level_order = []
        while q:
            cur = q.popleft()
            level_order.append(cur.val)
            
            if cur.left:
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.left)
        return res