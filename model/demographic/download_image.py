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
    # print(id)
    
    final_path = (re.split("/",images[1])[-1])
    
    image_url_final = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+final_path
    # print(image_url_final)
    return image_url_final

# print(get_image(11))