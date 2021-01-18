class Product:
    # name: string, price: double, amount: int
    def __init__(self, name, price, amount):
        self.__name = name 
        self.__price = price
        self.__amount = amount

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getAmount(self):
        return self.__amount

    # name: string
    def setName(self, name):
        self.__name = name

    # price: double
    def setPrice(self, price):
        self.__price = price

    # amount: int
    def setAmount(self, amount):
        self.__amount = amount