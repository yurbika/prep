class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        seen = {ele: secret.count(ele) for ele in secret}
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                a += 1
                if seen[guess[i]] <= 0:
                    b -= 1
                else:
                    seen[guess[i]] -= 1
            elif guess[i] in secret and seen[guess[i]] > 0:
                b += 1
                seen[guess[i]] -= 1

        return str(a)+'A'+str(b)+'B'
