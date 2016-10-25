from django.shortcuts import render,redirect
import random

def first_app(request):
    if 'numberoftimes' not in request.session:
        request.session['numberoftimes']=0
    word = randWord()
    RandomWords = {
    "RandomWord" : word
    }
    return render(request, 'first_app/index.html',RandomWords)

def generate(request):
    request.session['numberoftimes']+=1
    return redirect('/')


def randLetter():
    LETTER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    indletter = random.choice(LETTER)
    return indletter


def randWord():
    word = []
    randLength = random.randint(3,10)
    for i in range(randLength):
        indletter = randLetter()
        word += indletter
    word = "".join(str(x) for x in word)
    return word
