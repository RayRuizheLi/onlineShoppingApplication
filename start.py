from time import sleep

usernamePrompt = "What is your username: "
pwPrompt = "What is your password: " 

# Returns a hashmap of username and passwords 
def readLogins():
    logins = open("loginStore.txt", "r")

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

# Input: a dictionary of username password pairs 
def login(logins):
    print("Loging In")  
    username = input(usernamePrompt)
    pw = input(pwPrompt) 

    # Search for password and or username 
    # Can be modified to user hashing to reduce runtim 
    if username not in logins or logins[username] != pw:
        print("Login failed, sending to register")
        logins = register(logins)
        login(logins)

    
    print("Login success")

def main():
    loginPrompt = "Please select option: login | guest | register: "
    val = input(loginPrompt)
    logins = readLogins()
    
    if val != "guest":
        # register accounts 
        
        if val == "register":
            logins = register(logins); 

        
        # login time 
        login(logins)
        

    print("proceeding to shopping state") 

if __name__ == "__main__":
    main()
