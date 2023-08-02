import smtplib
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
#https://myaccount.google.com/u/0/lesssecureapps?pageId=none&pli=1
with open('mail id pass\mail.txt','r') as file:
 for line in file:
     for word in line.split():
         u=word.split(',')

def yuo(a):
    while True:
        with sr.Microphone() as source:
            engine.say(str(a))
            engine.runAndWait()
            audio = r.listen(source)

            try:
                print(r.recognize_google(audio).lower())
                sy = r.recognize_google(audio).lower()
                w = sy.split()
                si = "".join(w)+'@gmail.com'
                toaddrs = '{}'.format(si)
                fromaddr = '{}'.format(u[0])

                msg = "you know iam friday avilash's assistant this message is sent to you by my boss."

                username = '{}'.format(u[0])
                password = '{}'.format('ofecmxaxqwtmnwwa')
                with sr.Microphone() as source:
                    engine.say(' can i send the email to {}'.format(si))
                    engine.runAndWait()
                    audio = r.listen(source)
                    if r.recognize_google(audio).lower()=='yes':
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login(username, password)
                        server.sendmail(fromaddr, toaddrs, msg)
                        server.quit()
                        engine.say("email sent successfully boss.")
                        engine.runAndWait()


                    elif  r.recognize_google(audio).lower()=='no':
                        engine.say('email protocol cancelled')
                        engine.runAndWait()






                break
            except sr.UnknownValueError:
                print("Could not understand audio")
                continue


yuo('to whom should i send mail to ,can you spell the email domain')





#
#
#
#
