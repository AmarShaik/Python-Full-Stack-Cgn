# pip install gtts
# pip install speechrecognition
# pip install playsound==1.2.2
# pip install pyaudio

#Virtual Assistant
from gtts import gTTS #Google Text To Speech
import speech_recognition as sr
import playsound
from time import ctime
import os
import re
import uuid
import smtplib
import webbrowser

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio = r.listen(source, phrase_time_limit=5)
    data = ""
    try:
        data = r.recognize_google(audio, language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
listen()

#To respond back with audio
def respond(String):
    print(String)
    tts = gTTS(text=String, lang = 'en-US')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#Start giving actions
#Virtual Assistant actions
def virtual_assistant(data):
    "give your actions"
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    if "time" in data:
        listening = True
        respond(ctime())
    if "open google" in data.casefold():
        listening = True
        url = "https://www.google.com/"
        webbrowser.open(url)
        respond("Success")
    if "locate" in data:
        webbrowser.open('http://www.google.com/maps/search/' + data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))
    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen().lower()
        edict = {'amar':'shaikamar907@gmail.com'}
        toaddr = edict[to]
        respond("What is the subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject : {}\n\n{}'.format(subject,message)

        mail = smtplib.SMRP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()

        mail.login('shaikamar357@gmail.com', 'yqlh iwfx otmi pamw')
        mail.sendmail('shaikamar357@gmail.com', toaddr, content)
        mail.close()
        respond("Email Sent")
    if "stop" in data:
        listening = False
        print("Listening Stopped")
        respond("Okay done")
    try:
        return listening
    except UnboundLocalError:
        print("Timedout")
respond("Hey amar, how are you")
listening = True
while listening == True:
    data = listen()
    listening - virtual_assistant(data)
