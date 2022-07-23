from threading import Thread
import pyttsx3
import os
import datetime
import wikipedia
from time import sleep
import pyautogui
import numpy as np
from playsound import playsound
from sklearn.feature_extraction.text import CountVectorizer
from random import randint
import pyautogui as pa
from translate import Translator
from bs4 import BeautifulSoup
import requests
from GoogleNews import GoogleNews

print('Configuring...')

engine = pyttsx3.init()
list_commands = ['what time is it?', 'time', ':time', 'hi', 'hey', 'hello', 'hi ashia', 'hey ashia', 'hello ashia',
                 'good morning', 'hi good morning', 'hey good morning', 'good afternoon', 'hi good afternoon',
                 'hey good afternoon', 'good night', 'hi good night', 'hey good night', 'good evening',
                 'hi good evening', 'hey good evening', 'how are you?', "what's up?", 'how are you doing?',
                 'hi how are you?', 'hey how are you?', "hi what's up?", 'hi how are you doing', 'how are u?',
                 "i'm fine", "i'm okay", "i'm ok", "i'm good", "i'm sad", "i'm fine and you?", "i'm okay and you?",
                 "i'm good and you?", "i'm ok and you?", 'close explorer', 'what day is today?', 'date', 'day', ':date',
                 'thanks', 'thank you', 'thank u', 'open google', 'open youtube', 'google', 'youtube', 'joke',
                 'tell me a joke', 'hahaha', 'lol', 'hahah', 'haha', 'news', 'tell me new news', 'leave me updated',
                 'stop', 'gotcha', 'thumbs up', 'ok', 'how much is the dollar?', 'dollar', 'dollar price',
                 'erase everything i said today', 'erase what i just said', 'talk what you heard', 'privacy',
                 ':privacy', 'where are you from?', 'where are u from?', 'nice to meet you', 'nice to meet u',
                 'glad to meet you', 'glad to meet u', "what's you job?", "what's u job?", 'bye', 'bye bye', 'see you',
                 'see you later', 'see u later', 'see u', 'see ya', 'cya', 'goodbye', 'do you wanna date me?',
                 'date to me?', 'do you want to be my girlfriend?', 'i love you', 'i love u', 'i like you',
                 "i didn't understand what you meant", 'heads or tails', 'tails or heads', 'relax', 'help me relax',
                 'relax song', 'throw a coin', 'to be or not to be', 'lend me money', 'why are you ashia?',
                 "what's your name?", "it's good", "it's great", "it's ok", 'what is your favorite color?',
                 'who created you?', 'when you were born?', 'where were you born?', 'commands', ':commands', 'what are your most popular skills?', 'what can you do?']

def speak(text_speak):
    engine.say(text_speak)
    engine.runAndWait()


okay = False
command = ''

while True:
    try:
        arq = open('name.txt', 'a')
        arq.close()
        arq = open('name.txt', 'r')
        name = arq.read()
        if name == '':
            print('Account setup')
            print('-' * 20)
            name = str(input('Type your name: '))
            arq = open('name.txt', 'w')
            arq.write(name)
            arq.close()
            print(f"Hi {name}, I'm Ashia and I'm your virtual assistant. \n")
            print(
                '''You can insert the commands here and everything possible I will do!!\nTo get the list of all my commands just type ":commands"\nFor help contact us with support\nI'm sure I'll be very helpful to you 😊\n''')
            engine.say(
                f"Hi {name}, I'm Ashia and I'm your virtual assistant. " + '''You can insert the commands here and everything possible I will do! To get the list of all my commands just type :commands. for help contact us with support. I'm sure I'll be very helpful to you''')
            engine.runAndWait()
        arq.close()
        if okay:
            command = command.lower()
        else:
            command = (str(input(f'Your: ')).lower()).replace(',', '')
            first = ''
        okay = False
        if command[0:6] == 'ashia ':
            command = command[6:len(command)]
        text = len(command)
        if command == '' or command == ' ':
            continue
        if command == 'what time is it?' or command == 'time' or command == ':time':
            now = datetime.datetime.now()
            awnser = f'The time now is {now.hour}:{now.minute}'
            print(awnser)
            speak(awnser)
        elif command[text-13:text] == 'in portuguese':
            a = Translator(from_lang='english', to_lang='portuguese')
            result = a.translate(command[0:text-14])
            print(result)
            speak(result)
        elif 'weather' in command:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
            command = command.replace(' ', '+')
            def Weather():
                r = requests.get(
                    f'https://www.google.com/search?q={command}&oq={command}&aqs=chrome.0.35i3912j014j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
                    headers=headers)
                soup = BeautifulSoup(r.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                # print(soup.select('#wob_dts'))
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()

                print(location + '\n' + time + '\n' + info + '\n' + weather + '\xb0C')
                speak(location + '\n' + time + '\n' + info + '\n' + weather + '\xb0C')

            Weather()
        elif command[text-10:text] == 'in spanish':
            a = Translator(from_lang='english', to_lang='spanish')
            result = a.translate(command[0:text-14])
            print(result)
            speak(result)
        elif command[text-9:text] == 'in korean':
            a = Translator(from_lang='english', to_lang='korean')
            result = a.translate(command[0:text-14])
            print(result)
            speak(result)
        elif command[text-11:text] == 'in japanese':
            a = Translator(from_lang='english', to_lang='japanese')
            result = a.translate(command[0:text-14])
            print(result)
            speak(result)
        elif command[text-10:text] == 'in chinese':
            a = Translator(from_lang='english', to_lang='chinese')
            result = a.translate(command[0:text-14])
            print(result)
            speak(result)
        elif command[text-9:text] == 'in german':
            a = Translator(from_lang='english', to_lang='german')
            result = a.translate(command[0:text-14])
            print(result)
            speak(result)
        elif command[0:5] == 'bible':
            try:
                url = 'https://bible-api.com/'
                url_response = url + command[6:text].replace(' ', '')
                response = ((requests.get(url_response).json()).get('verses')[0]).get('text')
                print(response)
                speak(response)
            except:
                print('Could not find this, please make sure you typed or spoke correctly. (Example: John 3:16, is correct)')
                speak('Could not find this, please make sure you typed or spoke correctly. (Example: John 3:16, is correct)')
        elif command == 'commands' or command == ':commands' or command == 'what are your most popular skills?' or command == 'what can you do?':
            print('''\nHi, you requested the list of my commands, but they are many, I'll show the most coll and the most useful.

Time -> Shows the current time
Date -> Shows the current day
Open + {What you want to open} -> Opens whatever you want
Heads or Tails -> Play a coin and tells it to which side dropped
Joke -> Tell a joke or a pun for you
News -> Tell the main news of the day.
Play + {Music Name} -> You play the music you want (as long as you're in yours! List of songs!)
Stop -> Stop the music that is playing
Search + {What You Want Search} -> Search What do you want on Google
Search YouTube + {What you want Search} -> Search Whatever you want on YouTube
Open + {Program Name} -> Open the program you want
Open Web + {Site URL} -> Opens the site you want
Close + {The program name} -> Close the program you ask for
What's/Who is/Where is/History of/WHO + {What you want to know} -> shows the search result directly in the program.
Timer + {duration} + {unity} -> Creates a timer for the defined time
{text to translate} + in + {destination language} -> To translate any text. (Beta)

Out all this, you can still talk to me :") \n''')
            speak("Hi, you requested the list of my commands, but they are many, I'll show the most coll and the most useful. Out all this, you can still talk to me")
        elif command == 'hi' or command == 'hey' or command == 'hello' or command == 'hi ashia' or command == 'hey ashia' or command == 'hello ashia':
            print(f'Hi {name}, how are you?')
            speak(f'Hi {name}, how are you?')
        elif command == 'good morning' or command == 'hi, good morning' or command == 'hey, good morning':
            print('Good morning!')
            speak('Good morning!')
        elif command == 'good afternoon' or command == 'hi, good afternoon' or command == 'hey, good afternoon':
            print('Good afternoon!')
            speak('Good afternoon!')
        elif command == 'good evening' or command == 'hi, good evening' or command == 'hey, good evening':
            print('Good evening!')
            speak('Good evening!')
        elif command == 'good night' or command == 'hi, good night' or command == 'hey, good night':
            print('Good night!')
            speak('Good night!')
        elif command == 'how are you?' or command == "what's up" or command == 'how are you doing?' or command == 'hi how are you?' or command == "hi what's up" or command == 'hi how are you doing?':
            print("I'm OK")
            speak("I'm Okay")
        elif command == "i'm fine" or command == "i'm okay" or command == "i'm good":
            print("That's nice!")
            speak("That's nice!")
        elif command == "i'm fine and you?" or command == "i'm okay and you?" or command == "i'm good and you?" or command == "i'm ok and you?":
            print("That's nice! I'm OK")
            speak("That's nice! I'm okay")
        elif command == "i'm sad":
            print("What can I do to help?")
            speak("What can I do to help?")
        elif command == 'close explorer':
            name = 'explorer'
            print(f'Closing {name}')
            speak(f'Closing {name}')
            os.system(f"TASKKILL /F /IM {name}.exe")
            os.system(f"start \"\" explorer.exe")
        elif command == 'who created you?' or command == 'where were you born?' or command == 'when you were born?' or command == 'who created you' or command == 'where were you born' or command == 'when you were born':
            print(
                'I was not born, I was raised by a student named Gabriel Sozinho. My development began in August 2021, when he was 12 years old')
            speak(
                'I was not born, I was raised by a student named Gabriel Sozinho. My development began in August 2021, when he was 12 years old')
        elif command == 'what day is today?' or command == 'date' or command == 'day' or command == ':date':
            now = datetime.datetime.now()
            awnser = f'Today is {now.month} {now.day}, {now.year}'
            print(awnser)
            speak(awnser)
        elif command == 'thanks' or command == 'thank you' or command == 'thank u' or command == 'ok, thanks':
            print("You're welcome")
            speak("You're welcome")
        elif command == 'open google' or command == 'google':
            print('Opening Google... wait')
            os.system("start \"\" https://google.com")
            speak('Opening Google, wait')
        elif command == 'open youtube' or command == 'youtube':
            print('Opening YouTube... wait')
            os.system("start \"\" https://youtube.com")
            speak('Opening YouTube, wait')
        elif command == 'heads or tails' or command == 'tails or heads' or command == 'throw a coin':
            result = ['heads', 'tails']
            result = result[randint(0, 1)]
            print(result)
            speak(result)
        elif command == 'joke' or command == 'tell me a joke':
            jokes = ['What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.',
                     'I invented a new word! Plagiarism!', 'What does a cloud wear under his raincoat? Thunderwear.',
                     'What time is it when the clock strikes 13? Time to get a new clock.',
                     "Why did the dinosaur cross the road? Because the chicken wasn't born yet.",
                     "Why can't Elsa from Frozen have a balloon? Because she will “let it go, let it go.”",
                     "Why did the kid bring a ladder to school? Because she wanted to go to high school.",
                     "What building in your town has the most stories? The public library.",
                     "What's worse than finding a worm in your apple? Finding half a worm.",
                     "What falls in winter but never gets hurt? Snow.",
                     "What did the Dalmatian say after lunch? That hit the spot.",
                     "Why does a seagull fly over the sea? Because if it flew over the bay, it would be a baygull."]
            randint0 = randint(0, len(jokes) - 1)
            randint0 = (jokes[randint0])
            print(randint0)
            speak(randint0)
        elif command == 'hahaha' or command == 'lol' or command == 'hahah' or command == 'haha' or command == 'ha':
            print("If I made you laugh it means I'm funny hahaha")
            speak("If I made you laugh it means I'm funny hahaha")
        elif command == 'news' or command == 'tell me new news' or command == 'leave me updated':
            print('Getting news... Wait')
            speak('Getting news... Wait')
            try:
                googleNews = GoogleNews()
                googleNews.search('News')
                result = googleNews.result()
                for i in result:
                    title = i.get('title').replace(' ...', '...')
                    media = i.get('media')
                    print(title + ' - ' + str(media))
                    speak(title)
            except:
                print('You are offline')
                speak('You are offline')
        elif command[0:4] == 'play':
            text = len(command)
            os.system(f'TASKKILL /F /IM wmplayer.exe')
            os.system(f"TASKKILL /F /IM Music.UI.exe")
            print(f"Playing {command[5:text]}")
            speak(f"Playing {command[5:text].replace('_', ' ')}")
            os.system(f"start musics/{command[5:text].replace(' ', '_')}.mp3")
            sleep(.1)
            pyautogui.keyDown('alt')
            sleep(.1)
            pyautogui.press('tab')
            sleep(.1)
            pyautogui.keyUp('alt')
        elif command == 'stop':
            print(f'Stopping song')
            speak(f'Stopping song')
            os.system(f"TASKKILL /F /IM wmplayer.exe")
            os.system(f"TASKKILL /F /IM Music.UI.exe")
        elif command == "what is your favorite color?" or command == "what's your favorite color?":
            print('My favorite color is greenish red:)')
            speak('My favorite color is greenish red.')
        elif command[0:14] == 'search youtube':
            text = len(command)
            search = command[15:text]
            search = search.replace(' ', '+')
            print('Searching YouTube... wait')
            speak('Searching YouTube, wait')
            url = fr'https://www.youtube.com/results?search_query={search}'
            os.system(f"start \"\" {url}")
        elif command[0:6] == 'search':
            text = len(command)
            search = command[7:text]
            search = search.replace(' ', '+')
            print('Searching... wait')
            speak('Searching, wait')
            url = fr'https://www.google.com/search?q={search}'
            os.system(f"start \"\" {url}")
        elif command[0:8] == 'open web':
            text = len(command)
            url = command[9:text]
            print(f'Opening {url}... wait')
            os.system(f"start \"\" https://{url}")
            speak(f'Opening {url}, wait')
        elif command[0:4] == 'open':
            url = command[5:text]
            print(f'Opening {url}... wait')
            os.system(f"start \"\" {url}")
            speak(f'Opening {url}, wait')
        elif command[0:5] == 'close':
            name = command[6:text]
            print(f'Closing {name}')
            speak(f'Closing {name}')
            os.system(f"TASKKILL /F /IM {name}.exe")
        elif command[0:6] == "what's":
            print('Searching... Wait')
            speak('Searching, Wait!')
            try:
                search = (wikipedia.search(command[7:text]))[1]
                search = wikipedia.summary(search, sentences=3).replace('=', '')
                print(search)
                speak(search)

            except:
                print('Could not do this research')
                speak('Could not do this research')
        elif command[0:7] == 'where is':
            print('Searching... Wait')
            speak('Searching, Wait!')
            try:
                search = (wikipedia.search(command[8:text]))[1]
                search = wikipedia.summary(search, sentences=3).replace('=', '')
                print(search)
                speak(search)
            except:
                print('Could not do this research')
                speak('Could not do this research')
        elif command[0:10] == 'history of':
            print('Searching... Wait')
            speak('Searching, Wait!')
            try:
                search = (wikipedia.search(command[11:text]))[1]
                search = wikipedia.summary(search, sentences=3).replace('=', '')
                print(search)
                speak(search)
            except:
                print('Could not do this research')
                speak('Could not do this research')
        elif command[0:6] == 'who is':
            print('Searching... Wait')
            speak('Searching, Wait!')
            try:
                search = (wikipedia.search(command[7:text]))[1]
                search = wikipedia.summary(search, sentences=3).replace('=', '')
                print(search)
                speak(search)
            except:
                print('Could not do this research')
                speak('Could not do this research')
        elif command[0:3] == 'who':
            print('Searching... Wait')
            speak('Searching, Wait!')
            try:
                search = (wikipedia.search(command)[1])
                search = wikipedia.summary(search, sentences=3).replace('=', '')
                print(search)
                speak(search)
            except:
                print('Could not do this research')
                speak('Could not do this research')
        elif command == 'gotcha' or command == 'thumbs up' or command == 'ok' or command == 'i understand':
            print("It's Great")
            speak("It's great")
            continue
        elif command == 'how much is the dollar?' or command == 'dollar' or command == 'dollar price':
            print('1 dollar costs 1 dollar')
            speak('1 dollar costs 1 dollar')
        elif command == 'erase everything i said today' or command == 'erase what i just said' or command == 'talk what you heard' or command == 'privacy' or command == ':privacy':
            print(
                'Nothing of what you talk or write gets stored on my system, what can happen is your system temporarily save, but I have no control over it. Your privacy is my greatest desire')
            speak(
                'Nothing of what you talk or write gets stored on my system, what can happen is your system temporarily save, but I have no control over it. Your privacy is my greatest desire')
        elif command == 'where are you from?' or command == 'where are u from?':
            print("I'm from planet Earth")
            speak("I'm from planet Earth")
        elif command[0:6] == "what's":
            print('Searching... Wait')
            speak('Searching, Wait!')
            try:
                search = (wikipedia.search(command[7:text]))[1]
                search = wikipedia.summary(search, sentences=3).replace('=', '')
                print(search)
                speak(search)

            except:
                print('Could not do this research')
                speak('Could not do this research')
        elif command == 'nice to meet you' or command == 'nice to meet u':
            print('Nice to meet you too')
            speak('Nice to meet you too')
        elif command == 'glad to meet you' or command == 'glad to meet u':
            print('Glad to meet you too')
            speak('Glad to meet you too')
        elif command == "what's you job?" or command == "what's u job?":
            print("I'm your assistant")
            speak("I'm your assistant")
        elif command == 'bye' or command == 'bye bye' or command == 'see you' or command == 'see you later' or command == 'see u late' or command == 'see u' or command == 'see ya' or command == 'cya' or command == 'goodbye':
            print('Bye, see you later!')
            speak('bye, see you later!')
        elif command == 'do you wanna date me?' or command == 'date to me?' or command == 'do you want to be my girlfriend?':
            print('I hope your love is as sincere as my friendship for you')
            speak('I hope your love is as sincere as my friendship for you')
        elif command == 'i love you' or command == 'i love u' or command == 'i like you':
            print("It's good!")
            speak("It's good")
        elif command[0:5] == 'timer':
            def timer_minutes():
                sleep(command * 60)
                os.system(f"TASKKILL /F /IM wmplayer.exe")
                playsound('system/alarm.mp3')
                print('Timer triggered!')
                speak('Timer triggered!')
                pa.press('enter')
            def timer_seconds():
                sleep(command)
                os.system(f"TASKKILL /F /IM wmplayer.exe")
                playsound('system/alarm.mp3')
                print('Timer triggered!')
                speak('Timer triggered!')
                pa.press('enter')
            if command[text - 7:text] == 'minutes':
                command = float(command[text - 10:text - 8])
                print(f'Timer set for {command} minutes')
                speak(f'Timer set for {command} minutes')
                timer = Thread(target=timer_minutes)
                timer.start()
            elif command[text - 7:text] == 'seconds':
                command = float(command[text - 10:text - 8])
                print(f'Timer set for {command} seconds')
                speak(f'Timer set for {command} seconds')
                timer = Thread(target=timer_seconds)
                timer.start()
        elif command == "it's good" or command == "it's great" or command == "it's ok":
            print(':)')
            speak('')
        elif command[0:13] == 'wake me up in' or command[0:13] == 'wake up me in':
            text = len(command)
            def timer_minutes():
                sleep(command * 60)
                os.system(f"TASKKILL /F /IM wmplayer.exe")
                playsound('system/alarm.mp3')
                print('Timer triggered!')
                speak('Timer triggered!')
                pa.press('enter')
            def timer_seconds():
                sleep(command)
                os.system(f"TASKKILL /F /IM wmplayer.exe")
                playsound('system/alarm.mp3')
                print('Timer triggered!')
                speak('Timer triggered!')
                pa.press('enter')

            if command[text - 7:text] == 'minutes':
                command = float(command[14:text - 8])
                print(f'Timer set for {command} minutes')
                speak(f'Timer set for {command} minutes')
                timer = Thread(target=timer_minutes)
                timer.start()
        elif command == 'why are you ashia?' or command == "what's your name?":
            print('My name is Ashia. This name means “life” and “hope”.')
            speak('My name is Ashia. This name means “life” and “hope”.')
        elif command == 'relax' or command == 'help me relax' or command == 'relax sound':
            print(f"Relaxing")
            speak(f"Relaxing")
            try:
                os.system(f"TASKKILL /F /IM wmplayer.exe")
            except:
                print('')
            os.system(f"start musics/relax.mp3")
            sleep(.1)
            pyautogui.keyDown('alt')
            sleep(.1)
            pyautogui.press('tab')
            sleep(.1)
            pyautogui.keyUp('alt')
        elif command == "i didn't understand what you meant":
            print("I didn't understand what you meant")
            speak("I didn't understand what you meant")
        elif command == "to be or not to be":
            print("That is the question")
            speak("That is the question")
        elif command == 'lend me money':
            print("I can not lend money for you, but what I do, it's worth that everything")
            speak("I can not lend money for you, but what I do, it's worth that everything")
        else:
            n = 1
            value = False
            commandList = 'False'
            for command_spp in list_commands:
                counts = CountVectorizer(analyzer='word', ngram_range=(n, n))
                n_grams = counts.fit_transform([command, command_spp])
                intersection_list = np.amin(n_grams.toarray(), axis=0)
                intersection_count = np.sum(intersection_list)
                index_A = 0
                A_count = np.sum(n_grams.toarray()[index_A])
                if value < intersection_count / A_count:
                    value = intersection_count / A_count
                    commandList = command_spp
                    okay = True
            if first == command:
                okay = True
            else:
                command = commandList
                first = command
    except:
        print('Error')
        speak('Error')
