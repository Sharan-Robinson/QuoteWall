import os
import requests
import json
import shutil
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from Cliinit import getrandomquote
import random
import ctypes

def changewallpaper():
    response = requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1")

    data = json.loads(response.text)
    startstring = "https://bing.com/" + data["images"][0]['url']

    downloadimage = requests.get(startstring, stream=True)

    with open("Wallpaper.jpg", "wb") as f:
        shutil.copyfileobj(downloadimage.raw, f)

    img = Image.open('wallpaper.jpg')
    l1 = ImageDraw.Draw(img)

    randnum = random.SystemRandom()

    r = randnum.randint(0, 255)
    b = randnum.randint(0, 100)
    g = randnum.randint(0, 100)

    myfont = ImageFont.truetype('Algerian Regular.ttf', 65)

    l1.text((100, 100), getrandomquote(), font= myfont, fill=(r, b, g))


    img.save('WallQuote.jpg')

    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 2, os.path.abspath("WallQuote.jpg").encode(), 1)

changewallpaper()