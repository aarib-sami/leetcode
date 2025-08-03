class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scoreSet = { i : 0 for i in range(len(edges))}
        res = [0, 0]

        for i in range(len(edges)):
            scoreSet[edges[i]] = i + scoreSet.get(edges[i], 0)

        for i in range(len(edges)):
            if scoreSet[i] > res[0]:
                print(scoreSet[i], res[0])
                res = [scoreSet[i],i]

        return res[1]