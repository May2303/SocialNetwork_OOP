import SocialNetwork
import User
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Factory Pattern
class PostFactory:
    @staticmethod
    def publish_post(post_type, *args, **kwargs):
        if post_type == "text":
            return TextPost(*args, **kwargs)
        elif post_type == "image":
            return ImagePost(*args, **kwargs)
        elif post_type == "sale":
            return SalePost(*args, **kwargs)
        else:
            raise ValueError("Invalid post type")


class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.likes = set()
        self.comments = []

    def like(self, user):
        self.likes.add(user)
        user.update("Liked your post: {}".format(self.content))

    def comment(self, user, text):
        comment = "{}: {}".format(user.username, text)
        self.comments.append(comment)
        user.update("Commented on your post: {}".format(self.content))


class TextPost(Post):
    pass


class ImagePost(Post):
    def __init__(self, content, user, image_path):
        super().__init__(content, user)
        self.image_path = image_path

    def display(self):
        img = mpimg.imread(self.image_path)
        imgplot = plt.imshow(img)
        plt.show()


class SalePost(Post):
    def __init__(self, content, user, description, price, location):
        super().__init__(content, user)
        self.description = description
        self.price = price
        self.location = location
        self.sold = False

    def discount(self, percentage, password: str):
        if not self.sold:
           if password == self.user.password:
              self.price *= (100 - percentage) / 100
           else:
              print("this is not your post!!")
            
    def sold(self, password: str):
        self.sold = True
        
    def print_sold(self):
        print("this item sold by {}".format(self.user))

    def display(self):
        print("Sale Post: {} - ₪{} - Location: {} - available: {}".format(self.description, self.price, self.location, self.available))
