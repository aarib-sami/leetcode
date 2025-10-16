class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToAlpha = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }

        def dfs(curStr, i):
            if i == len(digits):
                res.append(curStr)
                return

            for letter in digitToAlpha[digits[i]]:
                curStr += letter
                dfs(curStr, i + 1)
                curStr = curStr[:-1]
            

        dfs("", 0)
        
        return res