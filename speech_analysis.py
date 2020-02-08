
import speech_recognition as sr
import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts ={
	"alias":('Киана'),
	"tbr":('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
	"cmds": {
		"ctime":('текущее время', 'сейчас времени','который час'),
		"radio":('включи музыку','воспроизведи радио', 'включи радио'),
		"stupid1":('расскажи анекдот','рассмеши меня', 'ты знаешь анекдот')
	}
}

# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
               #обращаются к Киане
            cmd = voice

            for x in opts['alias']:
                cmd=cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd=cmd.replace(x, "").strip()	

	        #распознаем и выполняем команду
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])	

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет соединение!")
                

#нечеткое распознование команды
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

    	for x in v:
    		vrt=fuzz.ratio(cmd,x)
    		if vrt>RC['percent']:
    			RC['cmd']=c
    			RC['percent']=vrt
    return RC			

def execute_cmd(cmd):
    if cmd == 'ctime':
    	now=datetime.datetime.now()
    	speak("Сейчас "+ str(now.hour)+":" + str(now.minute))

    elif cmd=='radio':
    	pass

    elif cmd =='stupid1':
    	speak("Как говорит мой разработчик")	
    else:
    	print('Команда не распознана, повторите!')	

# запуск
r=sr.Recognizer()
m=sr.Microphone(device_index =1)

with m as source:
	r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

#voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[1].id)


speak("Добрый день, хозяин")
speak("Киана  ждет указаний")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)
