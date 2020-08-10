class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while True:
            try:
                if S.index('#') == 0:
                    S = S[1:]
                else:
                    S = S[:S.index('#')-1]+S[S.index('#')+1:]
            except ValueError:
                break

        while True:
            try:
                if T.index('#') == 0:
                    T = T[1:]
                else:
                    T = T[:T.index('#')-1]+T[T.index('#')+1:]
            except ValueError:
                break
        return S == T
