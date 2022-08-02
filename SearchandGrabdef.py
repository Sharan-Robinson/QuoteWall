import time
import requests
from bs4 import BeautifulSoup


def loading():
    print("Searching.")
    time.sleep(.5)
    print("Searching..")
    time.sleep(.5)
    print("Searching...")

def leechQnA(topics):
    if topics == "veterans day":
        topics = "veterans-day"
    elif topics == "valentine's day":
        topics = "valentines-day"
    elif topics == "saint patrick's day":
        topics = "saint-patricks-day"
    elif topics == "new year's":
        topics = "new-years"
    elif topics == "mother's day":
        topics = "mothers-day"
    elif topics == "memorial day":
        topics = "memorial-day"
    else:
        pass

    finaldict = {}
    newpage = 1
    workedornot = True

    while workedornot:
        response = requests.get(f"https://www.brainyquote.com/topics/{topics}-quotes_{newpage}")
        if newpage > 1:
            for i in response.history:
                if response.url == f"https://www.brainyquote.com/topics/{topics}-quotes":
                    workedornot = False
        if workedornot == False:
            break

        soup = BeautifulSoup(response.text, features="html.parser")

        cout = []
        for i in soup.find_all("div", {"id": "qbc1"}):
            cout.append(i.text)
        entirelist = cout[0].split("\n")

        newlist = []
        for i in entirelist:
            if i != '':
                newlist.append(i)

        for i in newlist:
            if len(i) < 2:
                newlist.remove(i)

        Quotes = []
        Authors = []
        for i in newlist:
            if newlist.index(i) % 2 == 0:
                Quotes.append(i)

            else:
                Authors.append(i)

        dictstyle = dict(zip(Quotes, Authors))

        finaldict.update(dictstyle)

        newpage += 1


    Quotes = []
    Authors = []
    for i, j in finaldict.items():
        Quotes.append(i)
        Authors.append(j)

    return Quotes, Authors, finaldict
