class Solution:
    def toLowerCase(self, str: str) -> str:
        temp = [ord(i) for i in str]
        solution = ''
        for i in temp:
            if i < ord('a') and i >= ord('A'):
                i = chr(i + 32)
                solution += i
            else:
                solution += chr(i)

        return solution
