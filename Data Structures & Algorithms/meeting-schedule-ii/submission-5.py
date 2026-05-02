"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        heap = []
        count = 0
        for interval in intervals:
            if heap:
                lastMeeting = heap[0]
                if interval.start<lastMeeting:
                    count += 1
                else:
                    heapq.heappop(heap)
            heapq.heappush(heap,interval.end)
        return len(heap)

# [(0,40),(5,10),(15,20)]
# [(5,10),(15,20),(0,40)]