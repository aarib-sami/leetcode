class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r, c):
            if c < 0 or c >= COLS:
                return float('inf')
            
            if r == ROWS - 1:
                return matrix[r][c]

            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = matrix[r][c] + min(
                dfs(r + 1, c - 1),  
                dfs(r + 1, c),     
                dfs(r + 1, c + 1)  
            )

            return dp[(r, c)]

        return min(dfs(0, c) for c in range(COLS))