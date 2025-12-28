class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1

        nums.sort()

        for n in nums:
            if n == res:
                res = n + 1

        return res