class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd = 1, 1
        res = max(nums)

        for n in nums:
            tmp = maxProd
            maxProd = max(n * maxProd, n * minProd, n)
            minProd = max(n * minProd, n * tmp, n)
            res = max(res, maxProd)

        return res