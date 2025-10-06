class Solution:
    def reverse(self, x: int) -> int:
        numStr = str(x)
        resStr = []

        for i in range(len(numStr)-1, -1, -1):
            if numStr[i] == '-':
                resStr.insert(0, '-')
            else:
                resStr.append(numStr[i])

        resStr = "".join(resStr)

        if int(resStr) in range(-2**31, 2**31):
            return int(resStr)
        else:
            return 0