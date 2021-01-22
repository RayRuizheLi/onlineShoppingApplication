from catalog import Catalog
from product import Product

class Admin:

    def __init__(self):
        self.__catalog = Catalog()

    def addAdmin(self):
        print("Registering a new admin account.")

        username = input("What is your username: ")
        pw = input("What is your password: ") 

        f = open("adminLoginStore.txt", "a")
        f.write(username + "\n")
        f.write(pw + "\n") 
        f.close()

        print("Registration for admin finished")
    
    def modify(self):
        while(True):
            command = input("choose a command: list catalog (list) | add product (add) | remove product (remove) | register new admin (regi) | exit (exit)\n")

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
            elif command == "regi":
                self.addAdmin()
