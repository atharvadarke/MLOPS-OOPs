class Chatbook:
    def __init__(self):
        self.__username = "Default user"
        self.__password = ""
        self.logged_in = False
        self.menu()
    

    def getter(self):
        return self.__username
    
    def setter(self, name):
        self.__username = name

    def menu(self):
        user_input = input("""
                              1. Press 1 to signup
                              2. Press 2 to signin
                              3. Press 3 to write a post
                              4. Press 4 to message a friend
                              5. Press any other key to exit      
                                """)
        if(user_input == "1"):
            self.signup()
        elif(user_input == "2"):
            self.signin()
        elif(user_input == "3"):
            self.write_post()
        elif(user_input == "4"):
            pass
        else:
            exit()

    def signup(self):
        # set username
        name = input("Enter your username: ")

        # set password
        key = input("Set your password: ")

        self.__username = name
        self.__password = key
        self.menu()

    def signin(self):
        if self.__username == "" and self.__password == "":
            print("Please signup first")

        else:
            name = input("Enter your username: ")
            key = input("Enter your password: ")

            if self.__username == name and self.__password == key:
                print("Successfully signed in")
                self.logged_in = True

            else:
                print("Please input correct credentials")
        
        self.menu()


    def write_post(self):
        if self.logged_in == True:
            txt = input("Enter your message here: ")
            print(f"The following message posted:{txt}")

        else:
            print("Please signin first...")
            print("\n")

        self.menu()

    # def send_message(self):



chat = Chatbook()
c = Chatbook()
