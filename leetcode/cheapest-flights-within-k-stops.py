class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, c in flights:
            graph[s].append([d, c])
        
        costs = [float('inf')] * n
        costs[src] = 0

        for i in range(k+1):
            temp = costs.copy()
            for s in range(n):
                for d, c in graph[s]:
                    if costs[s] + c < temp[d]:
                        temp[d] = costs[s] + c
            costs = temp.copy()

        return costs[dst] if costs[dst] != float('inf') else -1