import pyautogui
import random
import time 
import json

WIDTH, HEIGHT = pyautogui.size()

def spam_click(amount, delay):
    for i in range(amount):
        x = random.randrange(1, WIDTH)
        y = random.randrange(1, HEIGHT)

        pyautogui.click(x, y)
        pyautogui.click()

        time.sleep(delay)

def threat_message(amount):
    messages_data = None
    with open("./src/keyboard-messages.json") as f:
        messages_data = json.load(f)
    
    for i in range(amount):
        message_chosen = random.choice(messages_data)
        open_app("notepad")
        time.sleep(1)

        for x in range(random.randrange(15, 20)):
            pyautogui.write(message_chosen)
            pyautogui.press("enter")

def open_app(app_name):
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write(app_name)
    time.sleep(0.5)
    pyautogui.press("enter")

threat_message(3)
