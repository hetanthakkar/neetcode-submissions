"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        count = 0
        intervals.sort(key = lambda x:x.start)
        for i,val in enumerate(intervals):
            if not heap:
                heapq.heappush(heap,(val.end,i))
            else:
                earliest = heap[0][0]
                if earliest>val.start:
                    heapq.heappush(heap,(val.end,i))
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(val.end,i))
        return len(heap)



        