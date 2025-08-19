class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        def maxInCol(c):
            res = float('-inf')
            for i in range(len(matrix)):
                res = max(res, matrix[i][c])
            return res
        
        for i in range(len(matrix)):
            minVal = min(matrix[i])
            for j in range(len(matrix[0])):
                if minVal == maxInCol(j):
                    res.append(minVal)

        return res