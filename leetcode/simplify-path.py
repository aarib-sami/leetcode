class Solution:
    def simplifyPath(self, path: str) -> str:
        parsedPath = path.split('/')
        for i in range(len(parsedPath)):
            parsedPath[i] =  parsedPath[i].replace('/', '')

        files = []

        for p in parsedPath:
            if not p or p == '.':
                continue
            elif p == "..":
                if files:
                    files.pop()
            else:
                files.append(p)

        res = ''
        
        for file in files:
            if file:
                res += '/' + file

        return '/' if not res else res