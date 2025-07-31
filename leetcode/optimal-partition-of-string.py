class Solution:
    def partitionString(self, s: str) -> int:
        stringSet = set()
        res = 1

        for c in s:
            if c in stringSet:
                res += 1
                stringSet.clear()
            
            stringSet.add(c)

        return res