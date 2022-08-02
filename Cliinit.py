#this is going to be where the prompt is going to be display on the command line.
from index import newlist
from SearchandGrabdef import leechQnA, loading
import random
import textwrap

def getvalue(value, dictionary):
    for i, j in dictionary.items():
        if value == i:
            return j
    return "not found"


numdict = dict(zip(range(1, len(newlist) + 1), newlist))


def getrandomquote():


        num = random.SystemRandom()
        randum1 = random.randint(0, len(newlist))



        givevale = getvalue(randum1, numdict)


        Quotes, Authors, dict = leechQnA(givevale)
        randnum = random.SystemRandom()

        num1 = randnum.randint(0,len(Quotes))

        newAuther = "\n -" + Authors[num1]

        return (textwrap.fill(Quotes[num1], 50)) + newAuther




