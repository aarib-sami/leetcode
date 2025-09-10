class Solution:
    def expand(self, s: str) -> List[str]:
        res = []

        def dfs(i, curString):
            if i >= len(s):
                res.append(curString)
                return

            if s[i] == '{':
                options = []
                i += 1
                while s[i] != '}':
                    if s[i].isalpha():
                        options.append(s[i])
                    i += 1
                i += 1
                options.sort()
                for option in options:
                    curString += option
                    dfs(i, curString)
                    curString = curString[:-1]
            else:
                curString += s[i]
                dfs(i + 1, curString)

        dfs(0, "")

        return res