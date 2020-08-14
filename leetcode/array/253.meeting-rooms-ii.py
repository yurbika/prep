class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        cnt = 0
        end = []
        intervals.sort(key=lambda i: i[0])
        for i in range(len(intervals)):
            if not end:
                cnt += 1
                end.append(intervals[i][1])
            elif intervals[i][0] not in end and min(end) > intervals[i][0]:
                cnt += 1
                end.append(intervals[i][1])
            else:
                end.pop(end.index(min(end)))
                end.append(intervals[i][1])

        return cnt
