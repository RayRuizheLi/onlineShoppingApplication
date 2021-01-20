from catalog import Catalog
from product import Product

class Admin:
    # username: string, password: string
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__catalog = Catalog()
    
    def modify(self):
        while(True):
            command = input("choose a command: list catalog (list) | add product (add) | remove product (remove) | exit (exit)\n")

            if command == "exit":
                break; 
            elif command == "list": 
                self.__catalog.listProducts()
            elif command == "add":
                name = input("name: ")
                price = input("price: ")
                amount = input("amount: ")
                prod = Product(name, price, amount)
                self.__catalog.addProduct(prod)
            elif command == "remove":
                name = input("name: ")
                self.__catalog.removeProduct(name)

admin = Admin("123", "123")
admin.modify()