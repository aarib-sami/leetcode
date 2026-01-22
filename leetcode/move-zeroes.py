class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = 0

        for i in range(1, len(nums)):
            while (i-1-zeroCount) in range(len(nums)) and nums[i-1-zeroCount] == 0:
                nums[i-zeroCount-1], nums[i-zeroCount] = nums[i-zeroCount], nums[i-zeroCount-1]
                zeroCount += 1
            zeroCount = 0