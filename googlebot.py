import webbrowser
import pyautogui as pg
import time

def Search(keyword):
    pg.write(keyword)

    pg.press('enter')

    time.sleep(2)

    for i in range(5):

        for i in range(5):
            pg.press('down')

        time.sleep(1)

    pg.press('home')
    time.sleep(1)
    pg.click(x=693, y=236)
    pg.press('backspace', presses=50)

# Open : Google
url = 'https://www.google.com'
webbrowser.open(url)
time.sleep(2)

Search('thailand travel')

# Key : New keyword
# Scroll : down and repeat
Search('japan travel')
Search('china travel')
