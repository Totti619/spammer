import pyautogui
import time
time.sleep(5)
text = open("text", "r")
for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")