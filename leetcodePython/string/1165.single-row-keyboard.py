class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        i = 0
        j = 0
        solution = 0
        for x in word:
            j = keyboard.index(x)
            solution += abs(j - i)
            i = j
        return solution
