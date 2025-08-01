class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            res.append([1] * i)

        if numRows <= 2:
            return res

        for i in range(2, numRows):
            p = 0
            for j in range(1, len(res[i])-1):
                res[i][j] = res[i-1][p] + res[i-1][p+1]
                p += 1       

        return res