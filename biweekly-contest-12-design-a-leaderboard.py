class Leaderboard:

    def __init__(self):
        self.players = set()
        self.player = []
        self.s = []

    def addScore(self, playerId: int, score: int) -> None:
        sc = 0
        if playerId in self.players:
            for i in range(len(self.player)):
                if self.player[i] == playerId:
                    self.player.pop(i)
                    sc = self.s.pop(i)
                    break
        else:
            self.players.add(playerId)
            sc = 0
        sc += score
        pos = bisect.bisect(self.s,sc)
        self.s.insert(pos,sc)
        self.player.insert(pos,playerId)
        #print(self.player)
        #print(self.s)


    def top(self, K: int) -> int:
        return sum(self.s[::-1][:K])

    def reset(self, playerId: int) -> None:
        for i in range(len(self.player)):
            if self.player[i] == playerId:
                t = i
                break
        self.player.pop(t)
        self.s.pop(t)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)