from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in edges:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])
        res = 0
        def dfs(node,visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor,visited)
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i,visited)
                res+=1
        return res
        