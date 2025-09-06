class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for f, t, p in flights:
            graph[f].append([t, p])

        cost = [float('inf')] * n
        cost[src] = 0

        for i in range(k+1):
            temp = cost.copy()
            for start in graph:
                for t, p in graph[start]:
                    temp[t] = min(temp[t], cost[t], cost[start]+p)
            cost = temp

        return cost[dst] if cost[dst] != float('inf') else -1