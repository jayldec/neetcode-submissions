class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d={i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            d[u].append(v)

        visited=set()
        path=set()
        def dfs(node):
            if node in path:
                return False 
            if node in visited:
                return True
            path.add(node)
            print(node)
            for nei in d[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visited.add(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
