# ---------------IMPORTS-----------------
import pyautogui
import time

# ----------------PEGAR PIXEL------------------
time.sleep(2)
print(pyautogui.position())


# ---------------SABER AS TECLAS-----------------
print(pyautogui.KEYBOARD_KEYS)


# ---------------FUNC SCROLL JA PRONTA-----------------
def scroll():
    pyautogui.scroll(-600)