from admin import Admin  
from shoppingCart import ShoppingCart 

usernamePrompt = "What is your username: "
pwPrompt = "What is your password: " 

# Input: the file name of logins
# Output: returns a hashmap of username and passwords 
def readLogins(fileName):
    logins = open(fileName, "r")

    loginDict = {}

    while True:
        line1 = logins.readline()
        line2 = logins.readline()

        if not line1:
            break
        
        line1 = line1.rstrip("\n")
        line2 = line2.rstrip("\n")

        loginDict[line1] = line2 

    return loginDict

# Input: a dictionary of username password pairs 
# Output: returns dictionary updated with new pw and un
def register(logins):
    print("Registering a new account.")

    username = input(usernamePrompt)
    pw = input(pwPrompt) 

    f = open("loginStore.txt", "a")
    f.write(username + "\n")
    f.write(pw + "\n") 
    f.close()

    logins[username] = pw

    return logins

# Input: a dictionary of username password pairs, boolean for is admin
# Return: if login is successful for admin. If normal, always go to register
def login(logins, isAdmin):
    print("Loging In")  
    username = input(usernamePrompt)
    pw = input(pwPrompt) 

    if isAdmin:
        if username not in logins or logins[username] != pw:
            print("Admin login failed")
            return False
        else:
            print("Admin login success")
            return True

    # Search for password and or username 
    # Can be modified to user hashing to reduce runtim 
    if username not in logins or logins[username] != pw:
        print("Login failed, sending to register")
        logins = register(logins)
        login(logins, False)
    
    print("Login success")
    return True 

def main():
    loginPrompt = "Please select option: login | guest | register | admin: "
    val = input(loginPrompt)
    logins = readLogins("loginStore.txt")
    adminLogins = readLogins("adminLoginStore.txt")

    global isGuest 
    isGuest = True
    
    if val == "login" or val == "register":
        # register accounts 
        if val == "register":
            logins = register(logins); 
        
        # login time 
        login(logins, False)

        isGuest = False
        
    elif val == "admin":
        isSuccess = login(adminLogins, True)
        
        if(not isSuccess):
            exit()

        admin = Admin()     
        admin.modify()

        print("Exiting admin session")

        exit()


    cart = ShoppingCart(isGuest)
    cart.startShopping()

if __name__ == "__main__":
    main()
