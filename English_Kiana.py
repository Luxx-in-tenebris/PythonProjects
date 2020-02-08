import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
#import  python-vlc
import urllib
import urllib3
import json
from bs4 import BeautifulSoup as soup
import urllib3 
import  wikipedia
import  random 
import time
import pyttsx3
import transliterate

#метод, который будет интерпретировать голосовой ответ пользователя:
def MyCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Скажите что-нибудь...')
        #r.pause_threshold=1 #задержка одна секунда
        r.adjust_for_ambient_noise(source,duration=1) #избавление от лишнего ума и помех в голосе
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language = "ru-RU").lower()
            print('Вы сказали: '+ command +'\n')
            #рекурсия, на случай если Киана не распознала речь
        except sr.UnknownValueError:
            print('Не могу разобрать, что вы сказали, скажите еще раз')
            command=MyCommand
        return command

#метод, который будет преобразовывать текст в речь
def KianaResponse(audio):
    print(audio)
    speak_engine.say(audio)
    speak_engine.runAndWait()
    speak_engine.stop()
    #for line in audio.splitlines():
    #    os.system("say"+audio)


def Assistant(command):
    #открыть ссылку    
    if 'открой' in command:
        command=command.replace('открой','open')    
        reg_ex = re.search('open (.+)',command) #transliterate.translit(command, reversed=True))
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            #KianaResponse('The website you have requested has been opened for you Sir.')
            KianaResponse('Питон при всём при том, заходя в дом на пол плюём, извините, уже открываю '+url)
        else:
            pass
    elif 'скажи мне о'in command:
        translate(command,'en')
        reg_ex = re.search('tell me about (.*)', translate(command,'en'))
        try:
            if reg_ex:
                topic=reg_ex.group(1)
                page=wikipedia.page(topic)
                
                KianaResponse(translate(page.content[:500].encode('utf-8'),'ru'))
        except Exception as e:
            KianaResponse(e)
    elif 'существует' in command:

        webbrowser.open('https://yopta.space/')
        KianaResponse('Йоптаскрипт позволит чётким пацанам быстро влиться в ряды программистов и процесс разработки')
    elif 'play me a song' in command:
        #path='/Users/Valentin/documents/python/Video'
        #folder = path
        #for the_file in os.listdir(folder):
        #    file_path= os.path.join(folder, the_file)
        #    try:
        #        if os.path.isfile(file_path):
         #           os.unlink(file_path)
        #    except Exception as e:
        #        print(e)
        KianaResponse('Какую песню сыграть?')
        mysong=MyCommand()
        if mysong:
            flag=0
            url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
            #webbrowser.open(url)
            response=urllib.request.urlopen(url)
            html = response.read()
            soup1 = soup(html,"lxml")
            url_list = []
            for video in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                #if ('https://www.youtube.com' + video['href']).startswith("https://www.youtube.com/watch?v="):
                #    flag = 1
                    final_url = 'https://www.youtube.com' + video['href']
                #    url_list.append(final_url)
                    url_list.append(final_url)
            print(url_list)
            #url = url_list[0]
           #ydl_opts = {}
            #ydl_opts={}
           # os.chdir(path)
            #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
               # ydl.download([url])
            #webbrowser.open(url)


        KianaResponse('Нашлась такая песня')
def translate(text,to_language):
    if 'ru' in to_language:
        lang = 'en-ru' 
    elif 'en' in to_language:
        lang = 'ru-en' 
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
    key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97' 
    
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang}) 
    # Выводим результат 
    return( json.loads(r.text)['text'][0])



speak_engine = pyttsx3.init()

 # Перебрать голоса и вывести параметры каждого

#KianaResponse('Hi User, I am Kiana and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')

KianaResponse('Говори')
while True:
    Assistant(MyCommand())










