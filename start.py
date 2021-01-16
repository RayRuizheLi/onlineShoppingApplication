from time import sleep

def main():
    loginPrompt = "Please select option: login | guest | register: "
    val = input(loginPrompt)
    
    if val != "guest":
        # register accounts 
        usernamePrompt = "What is your username: "
        pwPrompt = "What is your password: " 
        
        if val == "register":
            label: register
            print("Registering a new account.")

            username = input(usernamePrompt)
            pw = input(pwPrompt) 

            f = open("loginStore.txt", "a")
            f.write(username + "\n")
            f.write(pw + "\n") 
            f.write("----" + "\n")
            f.close()
        
        # login time 
        username = input(usernamePrompt)
        pw = input(pwPrompt) 

        # Search for password and or username 
        # Can be modified to user hashing to reduce runtim 
        users = open("loginStore.txt", "r")
        
        while True:
            line1 = users.readline()
            line2 = users.readline()
            line3 = users.readline()
            
            if not line1:
                goto: register
                break

            if line1 == username and line2 == pw: 
                break

    print("proceeding to shopping state") 

if __name__ == "__main__":
    main()
