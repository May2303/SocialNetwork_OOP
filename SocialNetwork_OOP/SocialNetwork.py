import string
from abc import ABCMeta, abstractstaticmethod
import SocialNetwork
import User
import Post

#singlton is appropriate in this case
class ISocialNetwork(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_name():
        """implement in child class"""




class myNetwork(ISocialNetwork):
    __instance = None
    listOfUsers = []
    listOfPasswords= []

    @staticmethod
    def get_name():
        if myNetwork.__instance == None:
            return None
        return myNetwork.__instance.name

    def __init__(self, name):
        if(myNetwork.__instance != None):
            raise Exception("Already have a network")
        self.name = name
        myNetwork.__instance = self


    @staticmethod
    def print_success():
        print(f"The social network {myNetwork.get_name} was created!")



    #u1 = network.sign_up("Alice", "pass1")
    def sign_up(self, username, password):
        if(password in self.listOfPasswords or len(password)>9 or len(password)<3):
            raise Exception("This Password is not secure, try another ")
        new_user = User.User(username, password)
        self.listOfUsers.append(new_user)
        self.listOfPasswords.append(password)
        return new_user
    
    

    #####################################################################################################3

    def log_in(self, name, password):
        if name in self.users:
            self.net_log = True

    def log_out(self, name):
        self.net_log = True

    def sigh_in(self, name, password):
        if name not in self.users:
            if 4 <= password <= 8:
                self.add_user(name)

    # add all the users of this network
    def add_user(self, user):
        self.users.append(user)

    # add all the posts of this network
    def add_post(self, post):
        SocialNetwork.User.User.post(post)


def display_notifications(self, user):
    # Display notifications for the given user
    for notification in user.notifications:
        print(notification)
