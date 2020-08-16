class Solution:
    def createCombinations(self, digit, combinations):
        comb = []
        for i in digit:
            for j in combinations:
                comb.append(i+j)
        return comb

    def recursion(self, digits, buttons, combinations):
        if len(digits) == 2:
            return self.createCombinations(
                buttons[digits[0]], buttons[digits[1]])

        combinations = self.createCombinations(self.recursion(
            digits[:-1], buttons, combinations), buttons[digits[-1]])
        return combinations

    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'}
        if digits == '':
            return []
        if len(digits) == 1:
            return [i for i in table[digits[0]]]
        combinations = self.recursion(digits, table, [])
        return combinations
