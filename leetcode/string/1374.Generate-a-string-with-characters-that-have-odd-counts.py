class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        if n % 2 == 0:
            return ("a"*(n-1))+("b")
        else:
            string = ("a"*(n-2))
            n -= n-2
            while n != 0:
                string = string + chr(ord('a')+n)
                n -= 1
            return string
