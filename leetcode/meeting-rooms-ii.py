class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = res = 0

        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        start.sort()
        end.sort()

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]: 
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            res = max(res, rooms)

        return res