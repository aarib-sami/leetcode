class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        res = 0
        stack = []
        stack.append([0, 0])

        while stack:
            i, j = stack.pop()
            if obstacleGrid[i][j] == 1:
                continue
            elif i == ROWS-1 and j == COLS-1:
                res += 1

            if i + 1 in range(ROWS):
                stack.append([i+1, j])
            if j + 1 in range(COLS):
                stack.append([i, j+1])

        return res