class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        s = s.upper()
        result = ''
        if len(s) == 0:
            return s

        if len(s) == 1:
            return s

        if len(s) % k != 0:
            result = s[:len(s) % k] + '-'

        for i in range(len(s[len(s) % k:])):
            if i % k == 0 and i != 0:
                result += '-'
                result += s[len(s) % k:][i]
            else:
                result += s[len(s) % k:][i]

        return result
