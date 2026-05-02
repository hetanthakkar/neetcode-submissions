from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in edges:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])
        visited = [-1] * n
        res = 0
        
        def dfs(node,component_number):
            visited[node] = component_number
            for neighbor in adj_list[node]:
                if visited[neighbor]== -1:
                    dfs(neighbor,component_number)
        
        for i in range(n):
            if visited[i]==-1:
                dfs(i,res)
                res+=1
        print(visited)
        return len(set(visited))
        