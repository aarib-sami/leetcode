class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            l, r = i, i
            palOdd = self.palindromLen(s, l, r)
            if len(palOdd) > len(res):
                res = palOdd

            l, r = i, i+1
            palEven = self.palindromLen(s, l, r)
            if len(palEven) > len(res):
                res = palEven

        return res
    
    def palindromLen(self, s, l, r):
        length = 0
        pal = ''
        while r in range(len(s)) and l in range(len(s)) and s[r] == s[l]:
            pal = s[l:r+1]
            length += 1
            r += 1
            l -= 1
        return pal if length > 0 else s[l]