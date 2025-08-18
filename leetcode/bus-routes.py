class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        seenSet = set()
        seenRoute = set()
        res = 0
        q = deque([source])

        while q:
            for i in range(len(q)):
                stop = q.popleft()

                if stop == target:
                    return res

                for routeIndex in graph[stop]:
                    if routeIndex in seenRoute:
                        continue
                    for newStop in routes[routeIndex]:
                        if newStop not in seenSet:
                            q.append(newStop)
                            seenSet.add(newStop)
                    seenRoute.add(routeIndex)
            
            res += 1

        return -1