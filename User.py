from SocialNetwork.Post import TextPost
from SocialNetwork.SocialNetwork import SocialNetwork
import Post


class Observer:
    def update(self, action):
        pass


class User(Observer):
    log = None

    # any new user has username, password
    # also has data - followers and posts
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.posts = []
        self.log = None

    def __new__(cls, *args, **kwargs):
        # Check if the user with the same username already exists
        existing_user = next((user for user in cls.users if user.username == kwargs.get('username')), None)
        if existing_user:
            return existing_user
        else:
            return super().__new__(cls)

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
