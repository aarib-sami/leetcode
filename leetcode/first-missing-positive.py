class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            index = val - 1

            if index in range(0, len(nums)):
                if nums[index] > 0:
                    nums[index] *= -1
                elif nums[index] == 0:
                    nums[index] = -(len(nums)+2)

        for i in range(0, len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1