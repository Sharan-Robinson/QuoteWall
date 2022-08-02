import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://www.brainyquote.com/topics")

soup = BeautifulSoup(response.text, features="html.parser")


topics = []
for i in soup.find_all("a", href = re.compile(r"\A/topics/")):
    topics.append(i.text)

samestring = ""
for i in topics:
    samestring +=i

samestring = samestring.split("\n")
newlist = []


[newlist.append(i.lower()) for i in samestring if len(i) >1]
#why did i use list comprehension all of a sudden? Because i can lmao.



