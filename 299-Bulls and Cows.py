class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        cnt = collections.Counter(secret)
        aPos = set()
        for i,c in enumerate(secret):
            if secret[i] == guess[i]:
                a += 1
                cnt[secret[i]] -= 1
                aPos.add(i)
        for i,c in enumerate(guess):
            if i in aPos:
                continue
            if cnt[guess[i]] > 0:
                b += 1
                cnt[guess[i]] -= 1
        return str(a) + 'A' + str(b) + 'B'