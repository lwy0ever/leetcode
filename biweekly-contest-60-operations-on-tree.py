class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        # children[i] = list,表示子节点的编号
        self.children = [[] for _ in range(n)]
        self.status = [-1] * n
        for i,p in enumerate(parent):
            if p == -1:
                continue
            self.children[p].append(i)
        #print(self.children)

    def lock(self, num: int, user: int) -> bool:
        if self.status[num] == -1:
            self.status[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] == user:
            self.status[num] = -1
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        # 需要先检查1和3,后操作解锁(条件2),避免不满足1和3的情况下有节点被解锁
        # 3,指定节点没有任何上锁的祖先节点
        p = num
        while p != -1:
            if self.status[p] != -1:
                return False
            p = self.parent[p]
            #print(p)
        # 1,指定节点当前状态为未上锁
        if self.status[num] == -1:
            # 2,指定节点至少有一个上锁状态的子孙节点
            # bfs
            cs = self.children[num]
            hasLockedNode = False
            while cs:
                newCS = []
                for c in cs:
                    if self.status[c] != -1:
                        hasLockedNode = True
                        self.status[c] = -1
                    newCS += self.children[c]
                cs = newCS
            if hasLockedNode:
                self.lock(num,user)
                return True
            else:
                return False
        else:
            return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)