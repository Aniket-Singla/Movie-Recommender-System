from bs4 import BeautifulSoup
import requests,urllib
import re, io
from PIL import Image, ImageTk
# import warnings
# warnings.filterwarnings("UserWarning")
def get_image(id):
    html_page = requests.get("https://www.themoviedb.org/movie/"+str(id))
    soup = BeautifulSoup(html_page.content, 'html.parser')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    final_path = (re.split("/",images[1])[-1])
    final = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+final_path
    raw_data = urllib.request.urlopen(final).read()
    im = Image.open(io.BytesIO(raw_data))
    width_org, height_org = im.size
    factor = 0.40
    width = int(width_org * factor)
    height = int(height_org * factor)
    im = im.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im)
    return image

