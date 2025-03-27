class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        We use a greedy approach. Affter sorting the intervals based on their start point, 
        Start tracing them from the first interval, when we have two overlapping intervals, drop
        the one with rightmost end point and increase the counter by one.
        '''
        intervals.sort(key = lambda x: x[0])
        counter = 0
        elem = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < elem[1]:
                #there is an overlap
                if intervals[i][1] < elem[1]:
                    elem = intervals[i]
                counter += 1
            else:
                elem = intervals[i]
        return counter