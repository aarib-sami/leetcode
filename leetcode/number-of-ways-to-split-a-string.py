class Solution:
    def numWays(self, s: str) -> int:
        numOne = 0
        n = len(s)
        mod = 10**9 + 7


        for c in s:
            if c == '1':
                numOne += 1

        if numOne == 0: return (((n - 1) * (n - 2)) // 2) % mod

        if numOne % 3 != 0: return 0

        first = second = counter = 0
        numPerGroup = numOne // 3

        for c in s:
            if c == '1':
                counter += 1

            if counter == numPerGroup:
                first += 1
            elif counter == 2 * numPerGroup:
                second += 1

        return ((first * second) % mod)