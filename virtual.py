import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import pyttsx3
import random
from time import ctime 
import datetime
import calendar
import webbrowser 
import ssl
import certifi
import time
import os 

import wikipedia

import subprocess
import pyautogui 
import bs4 as bs


class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() 
def record_audio(ask=""):
    with sr.Microphone() as source: 
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  
        except sr.UnknownValueError: 
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') 
        print(">>", voice_data.lower())
        return voice_data.lower()


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en-US') 
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) 
    playsound.playsound(audio_file) 
    print(asis_obj.name + ":", audio_string) 
    os.remove(audio_file) 
def getDate():
    
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
       'June', 'July', 'August', 'September', 'October', 'November',   
       'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']
   
    return ' ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'


def respond(voice_data):
    
    if there_exists(['galaxy''hey galaxy','hi galaxy','hello galaxy']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    
    if there_exists(["Tell ashi how much i love her"]):
        if person_obj.name:
            engine_speak("hello aashi, shiva loves you a lot")
        else:
            engine_speak("hello aashi, shiva loves you a lot ")

        if there_exists(["my name is"]):
           person_name = voice_data.split("is")[-1].strip()
           engine_speak("okay, i will remember that " + person_name)
           person_obj.setName(person_name) 
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) 

    
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    if there_exists(["what is today's date"]):
        get_date = getDate()
        
        engine_speak("Today is" + get_date)

    
    if there_exists(["what is the time","tell me the time","what time is it","time"]):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m' 
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour
           
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)
            engine_speak( ' '+ 'It is '+ str(hour)+ ':'+minute+' '+ meridiem)

     
    
    if there_exists(["search for","who is","price of"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + " on google")

    
    if there_exists(["definition of"]):
        search_term = voice_data.split("of")[-1]
        url = "https://en.wikipedia.org/wiki/" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on wikipedia")


    
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term )
    
     
    if there_exists([" how is today's weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is the weather")
     
     
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

     
    if there_exists([ "plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
     
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/dell/Pictures/Screenshots') 
    


    if there_exists(["exit", "quit", "goodbye", "bye"]):
        engine_speak("bye-have a nice day")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Galaxy'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Hello! My name is Galaxy? What can i do for you") 
    
    
    respond(voice_data) 