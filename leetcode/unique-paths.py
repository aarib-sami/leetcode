class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = {}
        res = 0

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            elif r == m-1 and c == n-1:
                return 1
            elif (r, c) in dp:
                return dp[(r, c)]
                
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        res = dfs(0,0)

        return res