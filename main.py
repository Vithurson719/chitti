import speech_recognition as sr

from gtts import gTTS
import os
from playsound import playsound
import webbrowser
import time

# text = "No more games Im change what you call rage"
language= "en"
#
# speech = gTTS(text = text, lang = language, slow = False)
# speech.save("text.mp3")
#
# os.system("start text.mp3")



r = sr.Recognizer()
r.energy_threshold=5000

x = 0


def searchSomething():
    audio1 = r.listen(source)

    text1 = r.recognize_google(audio1)
    url = 'https://google.com/search?q=' + text1
    webbrowser.get().open(url)
    print(text1)



while x == 0:

    with sr.Microphone() as source:
        print("Speak!")
        audio = r.listen(source)

        text = r.recognize_google(audio)

        if text == "what is your name":
            textAudio = "I am chitti."
            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("text1.mp3")
            playsound("text1.mp3")
        elif text == "search":
            textAudio = "what do you want to search vithu"
            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("text2.mp3")
            playsound("text2.mp3")
            searchSomething()
        elif text == "what is the time":
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            textAudio = "the time is displaying Vithurson"+current_time

            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("text2.mp3")
            playsound("text2.mp3")
        elif text == "who are you":
            textAudio = "I am chitti serves master"
            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("text3.mp3")
            playsound("text3.mp3")
        elif text == "my look":
            print(text)
            playsound('C:/Users/Microsoft/Downloads/alagu.mp3')
        elif text == "do you believe in God":
            textAudio = "who is god"
            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("god.mp3")
            playsound("god.mp3")
       
        elif text == "bank account":
            textAudio = "8100110938"
            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("text4.mp3")
            playsound("text4.mp3")

        
        elif text == "get up":

            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("hello.mp3")
            playsound("hello.mp3")

        else:
            textAudio = "Sorry sir! I could not hear your."
            speech = gTTS(text=textAudio, lang=language, slow=False)
            speech.save("text16.mp3")
            playsound("text16.mp3")




