class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        foundVal = set()
        replaceIndex = 0
        i = 0

        while i < len(nums):
            if nums[i] not in foundVal:
                nums[replaceIndex] = nums[i]
                replaceIndex += 1
                foundVal.add(nums[i])
            i += 1
        print(foundVal)
        return len(foundVal)