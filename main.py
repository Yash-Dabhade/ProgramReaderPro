# Text to speech
import os
import pyttsx3

# initial setting of the engine for conversion
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# selected voices[0] for men voice
print("Please enter Speed for Talking between 20-200::")
r = int(input())
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', r)


def TtoS(str):
    engine.say(str)
    engine.runAndWait()
    engine.stop()
    engine.save_to_file(str, 'REC.mp4')
    engine.runAndWait()


def filetoopen(filename):
    with open(filename, 'r') as f:
        filecontent = f.read()
    TtoS(filecontent)


print(
    'Enter  file name(if in present folder) or enter full path(Without [" "]):')
filename = input()
engine.say(
    "Hello  Friends. My name is Max and I am your Buddy !,Please Feel Free to talk with me. I was developed by Yash. How are you ? I will start reading in 3 seconds ,Please Wait")
engine.runAndWait()
filetoopen(filename)
input()
