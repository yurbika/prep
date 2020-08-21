class Solution:
    def maxDistToClosest(self, seats):
        solution = 0
        last = -1
        for i in range(len(seats)):
            if seats[i]:
                if last < 0:
                    solution = max(solution, i)
                else:
                    solution = max(solution, (i - last) / 2)
                last = i
        return int(max(solution, len(seats) - last - 1))
