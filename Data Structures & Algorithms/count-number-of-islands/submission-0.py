from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        vis = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            vis.add((r, c))
            q.append((r, c))
            while q:
                row , col = q.popleft()
                directions = [[1,0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and 
                        (r, c) not in vis):
                        q.append((r, c))
                        vis.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in vis:
                    bfs(r, c)
                    islands+=1
        return islands


        