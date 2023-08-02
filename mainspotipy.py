import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
r = sr.Recognizer()
def yuo(a):
    while True:
        with sr.Microphone() as source:
            engine.say(str(a))
            engine.runAndWait()
            audio = r.listen(source)

            try:
                print(r.recognize_google(audio).lower())
                if str(r.recognize_google(audio).lower()) == 'search music through albums':
                    import spot
                else:
                    import sample

                break
            except sr.UnknownValueError:
                print("Could not understand audio")
                continue




yuo('Search music through Albums or Search the top 10 HIT songs of that particular artist:')
