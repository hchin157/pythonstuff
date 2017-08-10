class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, password):
        self.user_name = name
        self.connections = []
        self.password = password

    def addName(self, user_name):
        self.user_name = user_name

    def addConnect(self, connection):
        self.connections.append(connection)

    def addPassword(self, password):
        self.password = password

    def getName(self):
        return self.user_name

    def getFriend(self):
        return self.friends

    def getPass(self):
        return self.password

class Network:
    # Define the fields and methods for your object here.
    def __init__(self, name):
        self.name = name
        self.users = []
        self.friends = []

    def addUser(self):
        user = input("Add a user: ")
        x = 0
        for i in self.users:
            if user != self.users[i]:
                x += 1
            else:
                continue
        if x == len(self.users):
            self.users.append(user)
            print("You've been added to the network.")
            return main()
        else:
            print("That name is taken.")
            a = input("Would you like to try a new name?")
            if a == 'yes' or a == 'y' :
                return addUser(self, user)
            elif a == 'no' or a == 'n':
                print("OK. Back we go!")
                return main()
            else:
                print("error")
                return main()

    def addFriend(self, user1, user2):
        z = False
        for i in user1.connections:
            if user2 == user1.connections[i]:
                z = True
                print ("It looks like you already know this person.")
                #return to main
            else:
                continue
        if z == False:
            if user1 not in Network.users.values() or user2 not in Network.users.values():
                print("That person doesn't exist.")
                return main()
            else:
                user1.addFriend(user2)
                user2.addFriend(user1)
                print ("You've been connected!")
                return main()

    def getUsers(self):
        print (self.users)

    def getConnect(self):
        print (self.connection)

    def getNumUsers(self):
        print (len(self.users))

def main():
    Matrix = Network("Neo")
    Testtt = User("New", "1234")
    #Mat#!!
    while 10 > 9:
        action = input("What would you like to do?")
        if action == "add user":
            Matrix.addUser()
        elif action == "add friend":
            xx = "What's your name? "
            yy = "What's your friend's name? "
            Matrix.addFriend(xx, yy)
        elif action == "get users":
            Matrix.getUsers()
        elif action == "get connections":
            Matrix.getConnect()
        elif action == "get number of users":
            Matrix.getNumUsers()
        elif action == "exit" or action == "get out":
            break
        else:
            return main()


# Runs your program.
if __name__ == '__main__':
    main()

# All methods for editing user attributes.
