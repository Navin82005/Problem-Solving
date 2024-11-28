from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        tmp_length = -1
        
        def bfs(node, graph, queue, level):
            if node == n - 1:
                print("Length:", level)
                return level
            
            while queue != []:
                head = queue.pop(0)
                # print("queue:", queue, "head:", head)
                queue.extend(graph[head])
                # print("After queue:", queue)
                return bfs(queue[0], graph, queue, level + 1)
        
        graph = {i : [i + 1] for i in range(n)}
        lengths = []
        for road in queries:
            graph[road[0]].append(road[-1])
            lengths.append(bfs(0, graph, [0], 0))

        return lengths


# Possible testcases
# print(Solution().shortestDistanceAfterQueries(n = 5, queries = [[2,4],[0,2],[0,4]]))
# print(Solution().shortestDistanceAfterQueries(n = 4, queries = [[0,3],[0,2]]))
print(Solution().shortestDistanceAfterQueries(n = 14, queries = [[0,6],[4,12]]))