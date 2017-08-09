class User:
    # Define the fields and methods for your object here.
    def __init__(self, name):
        self.user_name = name
        self.friends = []
        self.password = password

    def set_name (self, user_name):
        self.user_name = user_name
        user_name = input("Change your username here: ")

    def set_friend (self, friend):
        friend = input("Add a new friend here: ")
        self.friends.append(friend)

    def set_password (self, password):
        self.password = password

    def getName (self):
        return self.user_name

    def getFriend (self):
        return self.friends

    def getPass (self):
        return self.password

class Network:
    # Define the fields and methods for your object here.
    def __init__(self, name):
        self.name = name
        self.users = []

    def main():
    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
    main():

# All methods for editing user attributes.
