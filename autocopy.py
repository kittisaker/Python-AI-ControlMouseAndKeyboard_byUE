import pyautogui
import pyperclip
import time

time.sleep(3)

check = ''

for i in range(10):
    pyautogui.hotkey('ctrl', 'c')
    result = pyperclip.paste()
    print('---------------------', i, '---------------------')
    # print(result)

    if result != check:
        print(result)
        check = result

    time.sleep(2)