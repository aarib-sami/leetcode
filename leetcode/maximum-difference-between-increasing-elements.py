class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        minNum = float('inf')

        for i in range(len(nums)):
            minNum = min(minNum, nums[i])
            res = max(res, nums[i]-minNum)

        return res if res != 0 else -1