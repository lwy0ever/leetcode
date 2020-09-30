class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.person = dict()
        self.person[kingName] = {'child':[],'isAlive':True}

    def birth(self, parentName: str, childName: str) -> None:
        self.person[parentName]['child'].append(childName)
        self.person[childName] = {'child':[],'isAlive':True}


    def death(self, name: str) -> None:
        self.person[name]['isAlive'] = False


    def getInheritanceOrder(self) -> List[str]:
        def getChild(p):
            ans = []
            if self.person[p]['isAlive']:
                ans.append(p)
            for c in self.person[p]['child']:
                ans += getChild(c)
            return ans
        return getChild(self.king)



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()