class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreWithRank = [[score, index] for index, score in enumerate(score)]
        scoreWithRank.sort(reverse=True)
        res = [0] * len(score)

        for rank, (score, index) in enumerate(scoreWithRank):
            if rank == 2:
                res[index] = "Bronze Medal"
            elif rank == 1:
                res[index] = "Silver Medal"
            elif rank == 0:
                res[index] = "Gold Medal"
            else:
                res[index] = str(rank + 1)

        return res