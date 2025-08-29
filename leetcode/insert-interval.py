class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        def merge(intervals):
            intervals.sort()
            p1, p2 = 0, 1

            while p2 < len(intervals):
                int1 = intervals[p1]
                int2 = intervals[p2]
                if int2[0] <= int1[1]:
                    newInt = [min(int1[0], int2[0]), max((int1[1], int2[1]))]
                    intervals.remove(int2)
                    intervals[p1] = newInt
                    continue
                p1 += 1
                p2 += 1
            
            return intervals

        return merge(intervals)