import pyttsx3
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init()
rate = engine.getProperty('rate')
r = sr.Recognizer()
def guo(a):
    while True:
        with sr.Microphone() as source:
            engine.say(str(a))
            engine.runAndWait()
            audio = r.listen(source)

            try:
                sy = r.recognize_google(audio).lower()
                w = sy.split()
                si = 'www.google.com/search?q='+"+".join(w)

                controller = webbrowser.get()
                controller.open(si)
                break
            except sr.UnknownValueError:
                print("Could not understand audio")
                continue




guo('what you want to search ')
