from SocialNetwork.Post import TextPost
from SocialNetwork.SocialNetwork import SocialNetwork
import Post


class Observerable:


    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def register(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def unregister_all(self):
        self.observers.clear()

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
    


class Observer:
    def update(self, *args, **kwargs):
        pass



class User(Observer):

    # any new user has username, password
    # also has data - followers and posts
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.following = set()


    

    def follow(self, other_user):
        self.followers.add(other_user)
        other_user.following.add(self)
        print(f"{self.username} started following {other_user.username}")
        return
    
    
























####################################################### 
    # set the followers the user has
    def follow(self, other_user):
        if other_user != self:
            other_user.add_follower(self)

    # add followers to user
    def add_follower(self, follower):
        self.followers.add(follower)

    def post(self, content):
        post = TextPost(content, self)
        self.posts.append(post)
        Post.PostFactory.publish_post(post)
        self.notify_followers("User {} posted: {}".format(self.username, content))

    def notify_followers(self, message):
        for follower in self.followers:
            follower.update(message)

    def update(self, action):
        print("Notification for {}: {}".format(self.username, action))
