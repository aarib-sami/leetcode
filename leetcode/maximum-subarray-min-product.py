class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = float(-inf)

        for i in range(len(nums)):
            subArrayRes = 0
            minVal = float(inf)
            for j in range(i, len(nums)):
                minVal = min(minVal, nums[j])
                subArrayRes += nums[j]
                res = max(res, minVal * subArrayRes)

        return res % (10 ** 9 + 7)