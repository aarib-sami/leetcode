class Solution:
    def totalMoney(self, n: int) -> int:
        lastMonday = 0
        last = 0
        res = 0
        for i in range(n):
            if i % 7 == 0:
                val = lastMonday + 1
                res += val
                lastMonday = val
                last = lastMonday
            else:
                res += last + 1
                last += 1

        return res