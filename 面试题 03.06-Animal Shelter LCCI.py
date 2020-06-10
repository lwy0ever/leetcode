class AnimalShelf:

    def __init__(self):
        self.cat = []
        self.catIndex = 0
        self.dog = []
        self.dogIndex = 0


    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cat.append(animal[0])
        else:
            self.dog.append(animal[0])


    def dequeueAny(self) -> List[int]:
        r = 0
        if self.catIndex < len(self.cat):   # 有猫
            r = self.cat[self.catIndex]
            if self.dogIndex < len(self.dog):   # 有狗
                if r < self.dog[self.dogIndex]: # 猫老
                    self.catIndex += 1
                    return [r,0]
                else:   # 狗老
                    self.dogIndex += 1
                    return [self.dog[self.dogIndex - 1],1]
            else:   # 没有狗
                self.catIndex += 1
                return [r,0]
        else:   # 没有猫
            if self.dogIndex < len(self.dog):   # 有狗
                self.dogIndex += 1
                return [self.dog[self.dogIndex - 1],1]
            else:   # 没有狗
                return [-1,-1]
            


    def dequeueDog(self) -> List[int]:
        if self.dogIndex < len(self.dog):   # 有狗
            self.dogIndex += 1
            return [self.dog[self.dogIndex - 1],1]
        else:   # 没有狗
            return [-1,-1]


    def dequeueCat(self) -> List[int]:
        if self.catIndex < len(self.cat):   # 有猫
            self.catIndex += 1
            return [self.cat[self.catIndex - 1],0]
        else:
            return [-1,-1]



# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()