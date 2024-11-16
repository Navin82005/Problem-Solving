from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add(self, key, value):
        self.graph[key].append(value)
    
    def BFS(self, vertex):
        visited = [False] * (max(self.graph) + 1)
        # print(visited)
        queue = []
        
        queue.append(vertex)
        while queue:
            s = queue.pop(0)
            visited[s] = True
            print(s, end=" ")
            
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


bfs_graph = Graph()
bfs_graph.add(0, 1)
bfs_graph.add(0, 2)
bfs_graph.add(1, 2)
bfs_graph.add(2, 0)
bfs_graph.add(2, 3)
bfs_graph.add(3, 3)

bfs_graph.BFS(2)
