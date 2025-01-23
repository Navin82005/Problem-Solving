class Solution:
    # Function to return connected components of the graph
    def connectedcomponents(self, v, edges):
        # def check_all_visited():
        #     for i in range(v):
        #         if visited[i] == 0:
        #             return i
        #     return -1
        
        # graph = []
        
        # def bfs(start_node):
        #     q = [start_node]
        #     tmp = []
        #     while q != []:
        #         vx = q.pop(0)
        #         print(vx)
        #         if vx < len(edges):
        #             for i in edges[vx]:
        #                 if not visited[i]:
        #                     visited[i] = 1
        #                     q.append(i)
        #                     tmp += [i]
        #     graph.append(tmp)
        
        # visited = [0 for _ in range(v)]
        
        # node = check_all_visited()
        
        
        # while node != -1:
        #     print(node)
        #     bfs(node)
        #     node = check_all_visited()
        
        for i in range(len(edges) - 1):
            # print(edges[i], edges[i + 1], set(edges[i]).isdisjoint(set(edges[i + 1])))
            if not set(edges[i]).isdisjoint(set(edges[i + 1])):
                # print(set(edges[i]).union(set(edges[i + 1])))
                edges[i + 1] = set(edges[i]).union(set(edges[i + 1]))
                edges[i] = 0
        
        graph = []
        print(edges)
        for i in edges:
            if i != 0:
                graph.append(list(i))
        
        return graph

# 5
# 7
# 0 1
# 6 1
# 2 4
# 2 3
# 3 4

print(Solution().connectedcomponents(7, [[0, 1], [6, 1], [2, 4], [2, 3], [3, 4]]))

[[0, 1], [2, 1], [3, 4]]