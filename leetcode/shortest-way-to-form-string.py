class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res, targetIndex = 0, 0

        while targetIndex < len(target):
            prevIndex = targetIndex

            for c in source:
                if targetIndex < len(target) and c == target[targetIndex]: 
                    targetIndex += 1

            if targetIndex == prevIndex:
                return -1
            else:
                res += 1

        return res