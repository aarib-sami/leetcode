class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0

        i = 1
        groups = len(nums) // 3

        for _ in range(groups):
            res += nums[i]
            i += 2

        return res