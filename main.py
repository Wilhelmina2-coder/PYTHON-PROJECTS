import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)


def talk(text):  
    engine.say(text)
    engine.runAndWait()

def take_command():
   try:
    with sr.Microphone() as source:
        print('I am listening.....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'sulwe' in command: 
            command = command.replace('sulwe','')
            print(command)
   except:
      pass
   return command

def run_sulwe():
    command = take_command()
    print(command)
    if 'play' in command:
       song = command.replace('play', '')
       talk('playing' + song)
       pywhatkit.playonyt('song')
    elif 'time' in command:
       time = datetime.datetime.now().strftime('%I %M %p')
       print ('time')
       talk('current time is' + time)
    elif   'who is' in command:
       person = command.replace('who is', '')
       info = wikipedia.summary(person,1)
       print(info)
       talk(info)
    elif 'papa' in command:
       talk('Thank you for tomorrows lunch, If God permits, I shall really enjoy it. Akosua')
    elif 'good night' in command:
       talk('Dont forget to pray. Jesus loves you .Always remember you are a gem')
    elif 'joke' in command:
       talk(pyjokes.get_joke()) 
    else: 
       talk('Repeat that please')


while True:
  
   run_sulwe()