from PIL import Image
import requests
from io import BytesIO

class post:
    def __init__ (self , usrname , caption , url):
        self.usrname = usrname
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
        print (self.caption + " **" + self.usrname)
        print (self.likes , "likes")
        print ("Comments : ",self.comments)
class acc:
    def __init__ (self ,usrname , password):
        self.usrname = usrname
        self.password = password
class account :
    def __init__ (self , user_name , password):
        self.acc = acc (user_name , password)
        main.accs.append(self.acc)
        #self.posts = []
        self.post_number = 0
    def next_post (self):
        self.post_number += 1
    def previous_post (self):
        self.post_number -= 1
    def go_to_post (self , pn):
        self.post_number = pn
    def post (self , caption , url):
        post1 = post(self.acc.usrname , caption , url)
        main.postcount += 1
        #self.posts.append(post1)
        main.posts.insert(0,post1)
    def show (self):
        main.show(self.post_number)
    #def display (self):
        #print (self.acc.usrname , ":")
        #posts = self.posts.reverse()
        #for post in posts:
            #post.display()
    def view_acc (self , accname):
        main.view_account (accname)
    def like (self):
        main.like(self.post_number)   
    def comment (self , comment):
        main.comment(comment , self.acc.usrname , self.post_number)



class main :
    def __init__ (self):
        self.posts = []
        self.accs = []
        self.postcount = 0
    def view_account (self , accname):
        for post in self.posts:
            if post.usrname == accname :
                post.display()
    def show (self , post_number):
        self.posts[post_number].display()
    def like (self , post_number):
        self.posts[post_number].like()
    def comment (self , comment , usrname , post_number ):
        self.posts[post_number].comment(comment , usrname)
main = main()
asghar = account("asghar_021" , "gol")
akbar = account("gandi" , "shahe tehran")
sadra = account ("pil jiyan" , "batman")

asghar.post("tabiat" , "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg/220px-Ash_Tree_-_geograph.org.uk_-_590710.jpg")
akbar.show()
asghar.post("dirakht" , "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg/220px-Ash_Tree_-_geograph.org.uk_-_590710.jpg")
akbar.show()
akbar.like()
akbar.comment("in hamoone?")
akbar.next_post()
akbar.comment("vaaaay")
sadra.view_acc("asghar_021")
