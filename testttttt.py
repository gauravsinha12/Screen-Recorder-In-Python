import webbrowser
import pyautogui as pg
import time
import pyperclip as pc

webbrowser.open("https://meet.google.com/")
time.sleep(4)
pg.click(pg.locateCenterOnScreen('Capture.PNG'))
time.sleep(0.5)
pg.click(pg.locateCenterOnScreen('start.PNG'))
time.sleep(5)
pg.hotkey('ctrl','s')
time.sleep(0.5)
pg.hotkey('ctrl','c')
link = f"https://meet.google.com/{pc.paste()[7:(len(pc.paste())-5)]}"
