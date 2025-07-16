class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:        
        def isOverlap(s1, e1, s2, e2):
            if s2 < e1 and e2 > s1:
                return True
        
        for i in range(len(intervals)):
            s1, e1 = intervals[i]
            for j in range(i + 1, len(intervals)):
                s2, e2 = intervals[j]
                if isOverlap(s1, e1, s2, e2):
                    return False
        return True