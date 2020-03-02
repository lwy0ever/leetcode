class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.counter = 0
        self.d = discount
        self.n = n
        self.p = {}
        for i in range(len(products)):
            self.p[products[i]] = prices[i]

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        a = 0
        for i in range(len(product)):
            a += self.p[product[i]] * amount[i]
        self.counter += 1
        if self.counter == self.n:
            self.counter -= self.n
            a -= a * self.d / 100.0
        return a



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)