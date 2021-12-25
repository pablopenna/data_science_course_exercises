class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def getPrice(self):
        return self._price
    def getName(self):
        return self._name

d = dict()
while(True):
    n = input("Item name: ")
    if n == "-1":
        break
    p = float(input("Item price: "))
    i = Item(n,p)
    d.update({i.getName(): i.getPrice()})
    print(f"Shop summary: {d}")
