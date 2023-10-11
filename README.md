# Advance Mouse and Keyboard Control : Chapter-1 The Screen and Mouse Position

## Setup Enviroment
### install PyAutoGUI
```shell
pip install PyAutoGUI
```

### install pynput
```shell
pip install pynput
```

### PyAutoGUI : size()
```python
import pyautogui

print(pyautogui.size()) # Size(width=1920, height=1080)
```

### PyAutoGUI : position()

```python
import pyautogui

print(pyautogui.position())
# Point(x=0, y=0)
# Point(x=1849, y=1045)
```

### PyAutoGUI : moveTo(x, y)
```python
import pyautogui

pyautogui.moveTo(0, 0)
```

### PyAutoGUI : click()
```python
import pyautogui

pyautogui.moveTo(1826, 1047)
pyautogui.click()
```

```python
import pyautogui as pg
import time

time.sleep(3)

# pg.moveTo(1826, 1047)
pg.click(1826, 1047)
```

---