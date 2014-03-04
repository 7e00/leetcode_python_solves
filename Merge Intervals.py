# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x: x.start)
        mergelist = []
        pstart = intervals[0].start
        pend = intervals[0].end
        for each in intervals:
            if each.start <= pend:
                pend = max(pend, each.end)
            else:
                mergelist.append(Interval(pstart,pend))
                pstart = each.start
                pend = each.end
        mergelist.append(Interval(pstart,pend))
        return mergelist