# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        res = []
        for i in range(len(intervals)):
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
            else:
                break
        else:
            res.append(newInterval)
            return res
        if newInterval.end < intervals[i].start:
            res.append(newInterval)
            res.extend(intervals[i:])
        else:
            ps = min(intervals[i].start, newInterval.start)
            pe = max(intervals[i].end, newInterval.end)
            for j in range(i+1, len(intervals)):
                if pe >= intervals[j].start:
                    pe = max(pe, intervals[j].end)
                else:
                    res.append(Interval(ps, pe))
                    res.extend(intervals[j:])
                    break
            else:
                res.append(Interval(ps, pe))
        return res