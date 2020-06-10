class BrowserHistory:

    def __init__(self, homepage: str):
        self.his = [homepage]
        self.ind = 0


    def visit(self, url: str) -> None:
        self.ind += 1
        if len(self.his) <= self.ind:
            self.his.append(url)
        else:
            self.his[self.ind] = url
            self.his[self.ind + 1:] = []


    def back(self, steps: int) -> str:
        self.ind = max(0,self.ind - steps)
        return self.his[self.ind]


    def forward(self, steps: int) -> str:
        self.ind = min(len(self.his) - 1,self.ind + steps)
        return self.his[self.ind]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)