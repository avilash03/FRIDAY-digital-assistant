import pygame
import speech_recognition as sr

sd = ['stop', "ok"]

def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    r= sr.Recognizer()
    with sr.Microphone() as source:
        while pygame.mixer.music.get_busy():
            clock.tick(1000)
            print("should i stop:")
            audio = r.listen(source)
            print(audio)
            try:
                print("You said:- " + r.recognize_google(audio))
            except sr.UnknownValueError:
                 print("Could not understand audio")
                 continue
            if r.recognize_google(audio) in sd:
                 stopmusic()
                 break
            else:
                 continue

        #
        #
        #
        #
        #
        # isStop = input("Should I stop: ")
        # if isStop:
        #     stopmusic()
        # else:
        #     continue

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan

def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

def audp(file):
    try:
        initMixer()
        pmusic(file)
    except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
        stopmusic()
        print("\nPlay Stopped by user")
    except Exception:
        print("unknown error")
    print("Done")

audp('IM.mp3')
