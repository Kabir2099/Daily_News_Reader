import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def business():
    speak("Lets start business news...Please listen carefully..!")
    url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")


def science():
    speak("Lets start Science news...Please listen carefully..!")
    url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def sports():
    speak("Lets start sports news...Please listen carefully..!")
    url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def entertainment():
    speak("Lets start entertainment news...Please listen carefully..!")
    url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def technology():
    speak("Lets start technology news...Please listen carefully..!")
    url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def health():
    speak("Lets start Health news...Please listen carefully..!")
    url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")



if __name__=='__main__':
    speak("News for today ...")
    speak("Press 1 for business news.. press 2 for entertainment news..press 3 for health news...press 4 for sports news..press 5 for scince news..press 6 for technology news")
    while True:
        n=int(input("Press here :"))
        if(n==1):
            business()
        elif(n==2):
            entertainment()
        elif(n==3):
            health()
        elif(n==4):
            sports()
        elif(n==5):
            science()
        elif(n==6):
            technology()
        else:
            speak("Invalid press...!")
        speak("Are you want to continue to listening other news")
        t=input("press : ")
        if(t=='No'or t=='no'):
            break
        speak("Press 1 for business news.. press 2 for entertainment news..press 3 for health news...press 4 for sports news..press 5 for scince news..press 6 for technology news")
   







