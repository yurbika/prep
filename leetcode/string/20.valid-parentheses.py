class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        if len(s) < 2:
            return False

        need = ''
        valid = '({['

        for i in s:
            if i in valid:
                if i == '(':
                    need += ')'
                elif i == '[':
                    need += ']'
                elif i == '{':
                    need += '}'
            else:
                if need == '' or i != need[-1]:
                    return False
                else:
                    need = need[:-1]
        if need == '':
            return True
        else:
            return False
