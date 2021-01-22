import copy
from catalog import catalog

class ShoppingCart:
    # Input: boolean for if shopping cart is for guest
    def __init__(self, isGuest):
        self.__isGuest = isGuest
        self.__catalog = Catalog()
        self.__price = 0
        self.__cart = list()
    
    def browse(self):
        self.__catalog.listProducts()
    
    # Input: name of product and amount 
    def addProduct(self, name, quantity):
        prod = self.__catalog.getProduct(name)
        prod.setAmount(quantity)
        prod.setPrice(quantity * prod.getPrice())

        self.__cart.append(prod)

    # Input: name of product and amount 
    def removeProduct(self, name, quantity):
        for i in range(len(self.__cart)):
            if(self.__cart(i).getName() == name):
                self.__cart(i).setAmount(self.__cart(i).getAmount() - quantity)
                
                if self.__cart(i).getAmount() <= 0:
                    del self.__cart(i)
                    break

                self.__cart(i).setPrice(self.__cart(i).getAmount() * self.__cart(i).getPrice())

                break

    def listCart(self):
        for i in self.__cart:
            print("name: {}, total price: {}, amount: {}".format(i.getName(), i.getPrice(), i.getAmount()))

    def checkOut(self):
        if self.__isGuest: 
            print("Guest cannot checkout")
            return 

        for i in self.__cart:
            prod = copy.deepcopy(self.__catalog.getProduct(i.getName()))
            self.__catalog.removeProduct(i.getName)

            prod.setAmount(prod.getAmount() - i.getAmount())

            if(prod.getAmount() > 0):
                self.__catalog.addProduct(prod)

        print("Checkout complete, here is your receipt")

        self.listCart()
        
        exit()
    
    def startShopping(self):
        while(True):
            command = input("choose a command: list catalog (list) | list cart (cart) | remove product (remove) | add product (add) | checkout (check) | exit (exit)\n")

            if command == "exit":
                exit()
            elif command == "list": 
                self.__catalog.listProducts()
            elif commmand == "cart": 
                self.listCart()
            elif command == "add":
                name = input("name: ")
                amount = input("amount: ")
                self.addProduct(name, amount)
            elif command == "remove":
                name = input("name: ")
                self.removeProduct(name)
            elif command == "check":
                self.checkOut()



    

    

