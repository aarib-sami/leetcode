class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        res = float('inf')
        l, r = 0, max(nums)-1
        def costToChange(price):
            costNeeded = 0
            for p in range(len(nums)):
                difference = abs(price - nums[p])
                costNeeded += difference * cost[p]
            return costNeeded
        
        while l <= r:
            m = (l + r) // 2
            m1 = costToChange(m)
            m2 = costToChange(m+1)

            if m1 < m2:
                r = m - 1
                res = min(res, m1)
            else:
                res = min(res, m2)
                l = m + 1

        return res