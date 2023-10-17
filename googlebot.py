import webbrowser
import pyautogui as pg
import time

url = 'https://photofunia.com'
webbrowser.open(url)
time.sleep(2)

def generate_picture(keyword):
    pg.press('home')
    pg.click(x=350, y=341)
    pg.write("text", interval=0.25)
    pg.press('enter')
    time.sleep(2)

    for i in range(3):
        for i in range(7):
            pg.press('down')
        time.sleep(1)

    pg.moveTo(x=965, y=691)
    time.sleep(2)
    pg.click()
    time.sleep(1)

    for i in range(1):
        for i in range(7):
            pg.press('down')
        time.sleep(1)

    pg.moveTo(x=672, y=442)
    pg.click()
    pg.write(keyword, interval=0.25)
    pg.press('enter')
    time.sleep(2)

    pg.moveTo(x=1603, y=503)
    pg.click()
    time.sleep(2)
    pg.press('enter')
    time.sleep(4)


# generate_picture("Hello")
generate_picture("Python")

# pg.moveTo()
pg.click(x=1526, y=125)
time.sleep(2)
pg.press('enter')