class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        solution = []
        start = 0
        end = len(S)
        for i in S:
            if i == 'I':
                solution.append(start)
                start += 1
            else:
                solution.append(end)
                end -= 1
        solution.append(start)
        return solution
