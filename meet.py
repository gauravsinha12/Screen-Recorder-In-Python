import webbrowser
import pyautogui as pg
import time
from datetime import datetime
import pyperclip as pc
import pandas as pd
import smtplib


def meet():

    webbrowser.open("https://meet.google.com/")
    time.sleep(6)
    pg.click(pg.locateCenterOnScreen('Capture.PNG'))
    time.sleep(0.5)
    pg.click(pg.locateCenterOnScreen('start.PNG'))
    time.sleep(6)
    pg.hotkey('ctrl','s')
    time.sleep(0.5)
    pg.hotkey('ctrl','c')
    a = "https://meet.google.com/" + (pc.paste()[7:(len(pc.paste())-5)])
    SenderAddress = "g1ur1vsinha@gmail.com"
    password = "wubibhahpwdvlqum"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SenderAddress, password)
    msg = a
    subject = "please join this is a meet"
    body = "Subject: {}\n\n{}".format(subject,msg)
    # for email in emails:
    server.sendmail(SenderAddress, ["golubspr@gmail.com"], body)
    server.quit()
    

if __name__ == "__main__":

    print("Leave your pc to us we will do all the work just sit back and relax")
    print("If you want to conduct a meeting now please select  -  1 ")
    print("if you want to schedule the meeting then please select  -  2")
    b = int(input())
    if b==1:
        meet()
    else:
        tdelta=""
        try:
            s1 = input("enter the time to start meeting ")
            print("Enter the duration of meeting like if you want a meet for 1 hour then press  1")
            print("Enter the duration of meeting like if you want a meet for 30 minutes then press  2")
            print("")
            choice = int(input())
            if choice == 1:
                durations = 3600
            else:
                durations = 1800
            s2 = f"{datetime.now().time().hour}:{datetime.now().time().minute}:{datetime.now().time().second}"
            FMT = '%H:%M:%S'
            tsub = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
        except:
            print("Enter in this format for example (HH:MM:SS) :- 10:45:45")

        b = tsub.seconds
    time.sleep(b)
    meet()
