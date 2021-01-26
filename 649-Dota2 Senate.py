class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 策略:干掉自己身后最近的敌人
        # 如果身后没有敌人,则从队伍开头找
        Rlist = collections.deque()
        Dlist = collections.deque()
        n = len(senate)
        for i,c in enumerate(senate):
            if c == 'R':
                Rlist.append(i)
            else:
                Dlist.append(i)
        while True:
            if not Rlist:
                return 'Dire'
            if not Dlist:
                return 'Radiant'
            if Rlist[0] < Dlist[0]:
                Rlist.append(Rlist.popleft() + n)
                Dlist.popleft()
            else:
                Dlist.append(Dlist.popleft() + n)
                Rlist.popleft()