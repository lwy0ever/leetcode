class FileSystem:

    def __init__(self):
        self.fs = {}

    def create(self, path: str, value: int) -> bool:
        ps = list(path.split('/'))
        #print(ps[1:-1])
        cur = self.fs
        for p in ps[1:-1]:
            if p in cur:
                cur = cur[p][1]
            else:
                return False
        #print(cur)
        if ps[-1] in cur:
            return False
        else:
            cur[ps[-1]] = [value,{}]
            return True
        

    def get(self, path: str) -> int:
        ps = list(path.split('/'))
        cur = self.fs
        #print(cur)
        for p in ps[1:-1]:
            if p in cur:
                cur = cur[p][1]
            else:
                return -1
        #print(cur)
        if ps[-1] in cur:
            return cur[ps[-1]][0]
        else:
            return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)