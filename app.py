import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
# from audioPlay import audp
import time
import speech_recognition as sr
import pyowm

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate -int(25))
pt = ['initiating process, collecting data',"running files ,extracting engine"]
rtr = ['yes,want any help from me,boss', 'yes,is there any work for me to do ', 'yes,boss how can i help you with']
greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['how are you', 'how are you doing']
responses = ['Okay', "I'm fine"]
var2 = ['I was created by Avilash right in his  computer.']
var3 = ['what time is it', "what's the time", 'time']
var4 = ['who are you', 'what is your name', 'your good name', 'how can i call you', 'introduce yourself']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'drop the needle']
ty = ['who made you', 'who designed you']
v9=['initiate mail protocol','mail box']
vid4 = ['play video ', 'i want to watch a video','initiate tube protocol' ,'tube protocol']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing','thanks exit']
cmd9 = ['thank you', 'thanks']
fgh  = ['initiate music protocol','drop me to spotify']
spt =  ['initiate speed test','conduct speed test','what is my internet speed']
repfr9 = ['your welcome', 'glad i could help you', 'serving you is my pleasure']
m= ['initiate movie protocol','play movie']
fri="friday"
r = sr.Recognizer()
while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        engine.say(random.choice(pt))
        engine.runAndWait()
        audio = r.listen(source)
        try:
            if r.recognize_google(audio).lower() == 'friday':

                break
        except sr.UnknownValueError:
            print("Could not understand audio")
            continue
while True:
        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            engine.say(random.choice(rtr))
            engine.runAndWait()
            audio = r.listen(source)

            try:
                print("You said:- " + r.recognize_google(audio).lower())



            except sr.UnknownValueError:
                print("Could not understand audio")
                continue
        if r.recognize_google(audio) in greetings:
            random_greeting = random.choice(greetings)
            print(random_greeting)
            engine.say(random_greeting)
            engine.runAndWait()
        elif r.recognize_google(audio) in question:
            engine.say('I am fine')
            engine.runAndWait()


        elif r.recognize_google(audio) in cmd9:
            engine.say(random.choice(repfr9))
            engine.runAndWait()
        elif r.recognize_google(audio) in var4:
            engine.say("hi, i am friday, friday stands for Female Replacement Intelligent Digital Assistant Youth , I am avilash's augmented reality,security and digital assistant.")
            engine.runAndWait()
        elif r.recognize_google(audio) in vid4:

            import gui
        elif r.recognize_google(audio) in v9:
            engine.say('initiating mail protocol')
            engine.runAndWait()
            import emailME
        elif r.recognize_google(audio) in fgh:
            engine.say('initiating music protocol')
            engine.runAndWait()
            import mainspotipy

            engine.say('enjoy listening boss')
            engine.runAndWait()
            time.sleep(2)
            exit()

        elif r.recognize_google(audio) in spt:
            import rate








        elif r.recognize_google(audio) in cmd6:
            print('see you later')
            engine.say('see you later')
            engine.runAndWait()
            exit()
        elif r.recognize_google(audio) in cmd5:
            with sr.Microphone() as source:
                engine.say("for which city in india?")
                engine.runAndWait()
                audio = r.listen(source)

                try:
                    si = r.recognize_google(audio).lower().title() + ",IN"
                    print(si)



                except sr.UnknownValueError:
                    print("Could not understand audio")
                    continue
            owm= pyowm.OWM('3964503f91da507ed5d5c0465eb28b25')

            observation = owm.weather_at_place(si)
            observation_list = owm.weather_around_coords(12.972442, 77.580643)
            w = observation.get_weather()



            detailed_status = "overall status,," + (str(w).split("=")[-1].replace(">", ""))
            w.get_wind()
            w.get_humidity()
            w.get_temperature('celsius')
            windspeed = 'windspeed is {} kilometre per hour'.format(w.get_wind()['speed'])
            engine.say(windspeed)
            engine.runAndWait()
            direction = 'direction is about {} degree from north'.format(w.get_wind()['deg'])
            engine.say(direction)
            engine.runAndWait()
            humidity = 'humid content is about {} in the atmosphere.'.format(w.get_humidity())
            engine.say(humidity)
            engine.runAndWait()
            temperature = 'temperature is {} degree celsius'.format(w.get_temperature('celsius')['temp'])
            engine.say(temperature)
            engine.runAndWait()
            temperaturemax = 'temperature can occationally rise upto {} degree celsius'.format(float
                                                                                               (w.get_temperature('celsius')['temp_max'])+ float(1) )
            engine.say(temperaturemax)
            engine.runAndWait()
            temperaturemin = 'temperature may decrease to {} degree celsius as well'.format(float(
                w.get_temperature('celsius')['temp_min']) - float(1))
            engine.say(temperaturemin)
            engine.runAndWait()
            engine.say(detailed_status)
            engine.runAndWait()
        elif r.recognize_google(audio) in var3:
            import ntime
        elif r.recognize_google(audio) in cmd1:
            engine.say('initiating your default browser ')
            engine.runAndWait()
            import yui
            time.sleep(10)

           # webbrowser.open('www.google.com')
        elif r.recognize_google(audio) in ty:
            engine.say(random.choice(var2))
            engine.runAndWait()

        elif r.recognize_google(audio) in m:
            import movies


        else:
            engine.say("please wait")
            engine.runAndWait()
            print(wikipedia.summary(r.recognize_google(audio)))
            engine.say(wikipedia.summary(r.recognize_google(audio)))
            engine.runAndWait()
            # userInput3 = input("or else search in google")
            # webbrowser.open_new('www.google.com/search?q=' + userInput3)











