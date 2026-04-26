class Solution:
    def findNearestTreasure(self, row, col, grid):
        q = deque()
        q.append((row, col))
        n = len(grid)
        m = len(grid[0])
        distance = 0
        while q:
            row,col = q.popleft()
            x = [0, 0, -1, 1]
            y = [-1, 1, 0, 0]
            for i in range(4):
                newRow = row + x[i]
                newCol = col + y[i]
                if newRow >=0 and newCol>=0 and newRow < n and newCol < m:
                    if grid[newRow][newCol] == 2147483647:
                        grid[newRow][newCol] = min(grid[newRow][newCol], grid[row][col] + 1)
                        q.append((newRow,newCol))
                        
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        ans = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
         for j in range(m):
            if grid[i][j] == 0:
                q.append((i, j))

        n = len(grid)
        m = len(grid[0])
     
        while q:
            row,col = q.popleft()
            x = [0, 0, -1, 1]
            y = [-1, 1, 0, 0]
            for i in range(4):
                newRow = row + x[i]
                newCol = col + y[i]
                if newRow >=0 and newCol>=0 and newRow < n and newCol < m:
                    if grid[newRow][newCol] == 2147483647:
                        grid[newRow][newCol] = min(grid[newRow][newCol], grid[row][col] + 1)
                        q.append((newRow,newCol))

            