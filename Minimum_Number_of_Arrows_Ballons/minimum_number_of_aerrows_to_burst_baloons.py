class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        we need to find the overlapping intervals. All overlapping intervals, can be covered
        using one Ballon. To find the overlapping intervals, we can first sort the intervals
        based on their first indexes. Then find all overlappig intervals
        '''
        if not points:
            return 0

        sortedPoints = sorted(points, key=lambda x: x[0])
        
        numBaloons = 0
        start = sortedPoints[0][0] - 1
        end = sortedPoints[0][0] - 1
        for elem in sortedPoints:
            if elem[0] > start:
                start = elem[0]
                if start > end:
                    numBaloons += 1
                    end = elem[1]
            if elem[1] < end:
                end = elem[1]
        return numBaloons