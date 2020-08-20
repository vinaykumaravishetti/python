import os
import pyttsx3
from datetime import date
from datetime import datetime
print("Hi!whatsup!!:")
pyttsx3.speak("Hi!Hope your doing well...")
while(True):
        print("What can i do for you : ",end=" ")
        p=input()
        if((p=='q')or("stop" in p)or("exit" in p)or("quit" in p)):
                break
        if (("don't" in p) or("donot" in p)):
                print("Sorry! I didn't get you. Wait...What! you are checking me")
                pyttsx3.speak("Sorry! I didn't get you. Wait...What! you are checking me")
        else:
                if("vlc" in p):
                        pyttsx3.speak("vlc player is launching")
                        os.system("vlc")
                elif (("mediaplayer" in p)or("videoplayer" in p)):
                        pyttsx3.speak("wmplayer is launching")
                        os.system("wmplayer")
                elif (("chrome" in p)or("browser" in p)):
                        pyttsx3.speak("Chrome browser is opening")
                        os.system("chrome")
                elif (("notepad" in p)or ("editor" in p)):
                        pyttsx3.speak("Happy Writing")
                        os.system("notepad")
                elif (("calculator" in p)or("calci" in p)):
                        pyttsx3.speak("Calculator is launched")
                        os.system("calc")
                elif ("date" in p):
                        today = date.today()
                        print("Today's date:", today)
                elif ("time" in p):
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        print("Current Time =", current_time)
                elif (("browse" in p)or("open" in p)and("google" in p)):
                        pyttsx3.speak("Here you go")
                        os.system("chrome google.com")
                else:
                        print("Application is not found")
                        pyttsx3.speak("Application is not found")
print("Going to power saving mode")
pyttsx3.speak("Going to power saving mode")
