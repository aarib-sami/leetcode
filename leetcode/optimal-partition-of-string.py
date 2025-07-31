class Solution:
    def partitionString(self, s: str) -> int:
        stringSet = set()
        res = 0

        for c in s:
            if c in stringSet:
                print(c)
                res += 1
                stringSet = set()
            
            stringSet.add(c)

        return res+1