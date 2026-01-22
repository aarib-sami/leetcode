class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = 0
        lastOpenPos = deque([])

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                lastOpenPos.append(i)
            else:
                if lastOpenPos:
                    pos = lastOpenPos.popleft()
                    nums[pos] = nums[i]
                    lastOpenPos.append(i)
        
        for i in range(len(nums)-1, len(nums)-1-zeroCount, -1):
            nums[i] = 0