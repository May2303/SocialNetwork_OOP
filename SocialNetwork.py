import string
from abc import ABCMeta, abstractstaticmethod
import SocialNetwork
import User
import Post


class SocialNetwork():
    _current_network = None
    net_log = User.User.log
    users = [" "]

    def get_instance(self):
        if SocialNetwork._current_network is None:
            SocialNetwork("Defult Name")
            return self._current_network

    def __init__(self, _current_network):
        if SocialNetwork._current_network is not None:
            raise Exception("singleton can do this init only once!")
        else:
            SocialNetwork._current_network = self


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
