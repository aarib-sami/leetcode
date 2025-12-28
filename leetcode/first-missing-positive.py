class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1

        for i in range(1, len(nums)+2):
            if i not in nums:
                return i