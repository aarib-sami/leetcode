class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visit = set()
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        res = []

        def dfs(i, j, directionIndex):
            x, y = directions[directionIndex]

            if len(visit) == ROWS*COLS:
                return
            elif ((i+x, j+y) in visit or 
            i+x not in range(ROWS) or 
            j+y not in range(COLS)):
                directionIndex = (directionIndex + 1) % 4
            
            x, y = directions[directionIndex]

            visit.add((i, j))
            res.append(matrix[i][j])
            dfs(i+x, j+y, directionIndex)

        dfs(0, 0, 0)
        print(res)
        return res