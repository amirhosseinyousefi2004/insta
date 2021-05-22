from PIL import Image
import requests
from io import BytesIO

class post:
    def __init__ (self , ID , caption , url):
        self.ID = ID
        self.caption = caption
        self.url = url
        self.comments = []
        self.likes = 0
    def comment (self , comment , username):
        comment1 = comment + "  **" + username
        self.comments.append(comment1)
    def like (self):
        self.likes = self.likes + 1
    def display (self):
        url = self.url
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.show()
        print (self.caption + " **" + self.ID)
        print (self.likes , "likes")
        print ("Comments : ",self.comments)

class account :
    def __init__ (self , user_name , password):
        self.usrname = user_name
        self.password = password
        self.posts = []
        self.post_number = 0
    def next_post (self):
        self.post_number += 1
    def previous_post (self):
        self.post_number -= 1
    def post (self , caption , url):
        post1 = post(self.usrname , caption , url)
        self.posts.append(post1)
        main.posts.append(post1)
    def show (self):
        main.show(self.post_number)
    def like (self):
        main.like(self.post_number)   
    def comment (self , comment):
        main.comment(comment , self.usrname , self.post_number)



class main :
    #posts = []
    def __init__ (self):
        self.posts = []
    def show (self , post_number):
        self.posts[post_number].display()
    def like (self , post_number):
        self.posts[post_number].like()
    def comment (self , comment , usrname , post_number ):
        self.posts[post_number].comment(comment , usrname)
main = main()
asghar = account("asghar_021" , "83dune anar")
mhsn = account("gandi" , "mhsn shah tehran")
sadra = account ("pil jiyan" , "batman")

asghar.post("tabiat" , "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg/220px-Ash_Tree_-_geograph.org.uk_-_590710.jpg")
mhsn.show()
mhsn.like()
mhsn.comment("in derakhte toote")
sadra.show()
