# Advance Mouse and Keyboard Control : Chapter-3

## Using paprerclip
```shell
pip list
Package      Version
------------ -------
...
pyperclip    1.8.2
...

```

##

```shell
>python
>>> import pyperclip
>>> pyperclip.copy('Hello')

>>> t = pyperclip.paste()
>>> print(t)
ใช่เหรอ ไม่ได้โม้ใช่ไหม

```

##

```python
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
```


