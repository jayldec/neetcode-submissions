from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build graph (undirected)
        class Graph:
            def __init__(self, edges, n):
                self.neighbors = [[] for _ in range(n)]
                for s, d in edges:
                    self.neighbors[s].append(d)
                    self.neighbors[d].append(s)  # undirected, add both

        g = Graph(edges, n)
        visited = set()

        # DFS with parent tracking
        def dfs(node, parent):
            visited.add(node)
            for ne in g.neighbors[node]:
                if ne not in visited:
                    if not dfs(ne, node):
                        return False
                elif ne != parent:  # found a back edge -> cycle
                    return False
            return True

        # Must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # DFS from node 0
        if not dfs(0, -1):
            return False

        # Must visit all nodes
        return len(visited) == n
