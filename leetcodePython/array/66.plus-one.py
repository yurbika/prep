class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(str(i) for i in digits)
        num = str(int(num) + 1)
        digits = [int(i) for i in num]
        return digits
