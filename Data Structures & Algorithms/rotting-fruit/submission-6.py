from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        time = float("-inf")
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            popped = queue.popleft()
            i, j, minutes = popped
            time = max(minutes,time)
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    queue.append((ni, nj, minutes + 1))
                    grid[ni][nj] = 2

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time if time != float("-inf") else 0
        
