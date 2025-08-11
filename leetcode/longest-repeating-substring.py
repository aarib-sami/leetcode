class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        res = 0
        N = len(s)

        def dupSubstring(length):
            nonlocal res
            subSet = set()
            for i in range(0, N - length + 1):
                if s[i: i + length] in subSet:
                    res = length
                    return True
                else:
                    subSet.add(s[i: i + length])

            return False

        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            if dupSubstring(mid):
                l = mid + 1
            else:
                r = mid - 1

        return res