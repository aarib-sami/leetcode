class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        blocks = defaultdict(int)

        for x, y in coordinates:
            for i in range(max(0, x-1), min(m-1, x+1)):
                for j in range(max(0, y-1), min(n-1, y+1)):
                    blocks[(i, j)] += 1

        totalBlocks = (m-1) * (n-1)
        res[0] = totalBlocks - len(blocks)

        for count in blocks.values():
            res[count] += 1

        return res