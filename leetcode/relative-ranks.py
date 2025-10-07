class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        playerCount = len(score)
        minHeap = []
        placement = {}
        res = []

        for i, s in enumerate(score):
            heapq.heappush(minHeap, [s, i])

        counter = 0

        for i in range(playerCount):
            score, index = heapq.heappop(minHeap)
            if playerCount - i == 3:
                rank = "Bronze Medal"
            elif playerCount - i == 2:
                rank = "Silver Medal"
            elif playerCount - i == 1:
                rank = "Gold Medal"
            else:
                 rank = str(playerCount - i)
            
            placement[index] = rank

        for i in range(playerCount):
            res.append(placement[i])

        return res