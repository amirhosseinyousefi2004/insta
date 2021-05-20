from PIL import Image
import requests
from io import BytesIO

url = "https://images-na.ssl-images-amazon.com/images/I/91dYFuM4xfL.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image.show()
