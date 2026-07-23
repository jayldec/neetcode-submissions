class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class Graph:
            def __init__(self, edges, n):
                self.neighbors = [[] for _ in range(n)]
                for s, d in edges:
                    self.neighbors[s].append(d)
                    self.neighbors[d].append(s)  # undirected, add both

        g = Graph(edges, n)
        visited = set()

        # DFS with parent tracking
        def dfs(node):
            visited.add(node)
            for ne in g.neighbors[node]:
                if ne not in visited:
                    if not dfs(ne):
                        return False
                
            return True
        components=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components+=1
        return components