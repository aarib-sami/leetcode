class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        romanToDec = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        c = 0
        while c < len(s):
            numeral = ''
            for i in range(c, min(c+2, len(s))):
                numeral += s[i]
            if numeral in romanToDec:
                res += romanToDec[numeral]
                c += 2
            else:
                res += romanToDec[numeral[0]]
                c += 1

        return res