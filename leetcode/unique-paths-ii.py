class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(ROWS-1, COLS-1) : 1}

        def dfs(i, j):
            if (i not in range(ROWS) or 
            j not in range(COLS) or
            obstacleGrid[i][j] == 1):
                return 0
            elif i == ROWS-1 and j == COLS-1:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return dp[(i, j)]

        return dfs(0, 0)