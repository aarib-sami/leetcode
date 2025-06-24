class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keySet = set()
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                keySet.add(i)

        for i in range(len(nums)):
            for index in keySet:
                if abs(i-index) <= k:
                    res.append(i)
                    break

        return res