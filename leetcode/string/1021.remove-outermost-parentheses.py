class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        p = 0
        parts = []
        for i in range(len(S)):
            if S[i] == '(':
                count += 1
            elif S[i] == ')':
                count -= 1
            if count == 0:
                parts.append(S[p+1:i])
                p = i+1
                
        return ''.join(parts)