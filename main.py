import speech_recognition as sr
import pyttsx3;

import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

def response_func(msg):
    global kernel
    response = kernel.respond(msg)

    if response =="":
        response = "Don't know how to answer that one for now"

    return response

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print("Got it")
    print(r.recognize_google(audio))
    response = response_func(r.recognize_google(audio))

# recognize speech using Sphinx
try:
    #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    print("Sphinx thinks you said " + r.recognize_google(audio))
    engine = pyttsx3.init()
    engine.setProperty('voice', 'afrikaans')
    engine.say(response)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
