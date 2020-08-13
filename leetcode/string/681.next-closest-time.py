class Solution:
    def nextClosestTime(self, time: str) -> str:
        minutes = int(time.split(':')[0])*60 + int(time.split(':')[1])
        allowed = [int(x) for x in time if x != ':']
        while True:
            minutes = (minutes + 1) % (24 * 60)
            nextTime = [int(minutes/60/10), int(minutes/60 % 10),
                        int(minutes % 60/10), minutes % 60 % 10]

            valid = True
            for i in nextTime:
                if i not in allowed:
                    valid = False

            if valid:
                return f'{int(minutes/60):02d}:{minutes%60:02d}'
