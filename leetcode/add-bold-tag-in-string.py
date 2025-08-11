class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)
        res = ''

        for word in words:
            foundWord = s.find(word)
            wordLen = len(word)

            while foundWord != -1:
                for i in range(foundWord, foundWord+wordLen):
                    bold[i] = True
                foundWord = s.find(word, foundWord+1)
        i = 0
        while i < len(s):
            if bold[i] == True:
                res += '<b>'
                while i < len(s) and bold[i] == True:
                    res += s[i]
                    i += 1
                res += '</b>'
            else:
                res += s[i]
                i += 1        
        return res