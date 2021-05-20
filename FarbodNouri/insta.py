from PIL import Image
import requests
from io import BytesIO
class Account:
    def __init__(self,username,password):
        self.username = str(username)
        self.password = str(password)
        #TODO: generate an id

    def login(self):
        pass
        #login mikone :)
    
class User(Account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.posts = []
        self.followers = set()
        self.followings = set()
    
    def add_post(self, url):
        post = Post(url,self.username)
        self.posts.append(post)


class Post:
    def __init__(self,url,sender_username):
        self.url = url
        self.sender_username = sender_username
        self.comments = []
        self.likes = set()

    def add_like(self, user):
        assert isinstance(user,User), "Only users can like a post!"
        self.likes.add(user.username)

    def add_comment(self, user, content):
        assert isinstance(user,User), "Only users can leave a comment!"
        self.comments.append((user.username, content))

    def show_image(self):
        response = requests.get(self.url)
        image = Image.open(BytesIO(response.content))
        image.show()



if __name__ == '__main__':
    user1 = User(username= 'usr1', password= 'pass123')
    user1.add_post("https://images-na.ssl-images-amazon.com/images/I/91dYFuM4xfL.png")
    user1.posts[0].show_image()
