class UndergroundSystem:

    def __init__(self):
        self.ids = {}   # 存储在地铁站里的id,ids[id] = [stationName,t]
        self.ttl = {}   # ttl[(from,to)] = [total,num]  total表示总时间,num表示乘客数量


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = [stationName,t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.ids[id][0],stationName) not in self.ttl:
            self.ttl[(self.ids[id][0],stationName)] = [t - self.ids[id][1],1]
        else:
            self.ttl[(self.ids[id][0],stationName)] = [self.ttl[(self.ids[id][0],stationName)][0] + t - self.ids[id][1],self.ttl[(self.ids[id][0],stationName)][1] + 1]
        del self.ids[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ttl[(startStation,endStation)][0] / self.ttl[(startStation,endStation)][1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)