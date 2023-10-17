# Advance Mouse and Keyboard Control : Chapter-2

## Basic function
```python
def hello():
    print("Hello")


hello()
```

### function with for loop
```python
for i in range(3):
    print(i, 'hello')
# 0 hello
# 1 hello
# 2 hello
```

```python
def hello():
    for i in range(1, 6):
        print(i, 'hello')

hello()
# 1 hello
# 2 hello
# 3 hello
# 4 hello
# 5 hello
```

```python
def hello(n):
    for i in range(n):
        print(i, 'hello')

hello(2)
# 0 hello
# 1 hello
```

## Mouse and Keyboard function
```shell
Open : Google
Key : Keyword
Press : enter
Wait : 2 second
Scroll : Down
Stop : 2 second
Continue : Scroll Down
Repeat : 10
Goto : Top
Key : New keyword
Scroll : down and repeat
```

```python
import webbrowser
import pyautogui as pg
import time

def Search(keyword):
    # Key : Keyword
    # pg.write('thailand travel', interval=0.25)
    pg.write(keyword)

    # Press : enter
    pg.press('enter')

    # Wait : 2 second
    time.sleep(2)

    # Scroll : Down
    # pg.moveTo(1000, 600)

    for i in range(5):
        # Stop : 2 second
        # Continue : Scroll Down
        # Repeat : 10
        
        # pg.scroll(-1000)

        for i in range(5):
            pg.press('down')

        time.sleep(1)

    # Goto : Top
    # pyautogui.position()
    # Point(x=693, y=236)
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

```