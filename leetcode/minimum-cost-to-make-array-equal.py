class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        res = float('inf')
        
        def costToChange(price):
            costNeeded = 0
            for p in range(len(nums)):
                difference = abs(price - nums[p])
                costNeeded += difference * cost[p]
            return costNeeded
        
        for i in range(0, max(nums)+1):
            res = min(res, costToChange(i))

        return res