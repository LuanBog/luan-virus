import pyautogui
import random
import time 
import json
import string

# Set this to True if you're testing the script
pyautogui.FAILSAFE = False

WIDTH, HEIGHT = pyautogui.size()

def spam_click(amount, delay):
    for i in range(amount):
        x = random.randrange(1, WIDTH)
        y = random.randrange(1, HEIGHT)

        pyautogui.click(x, y)
       
        time.sleep(delay)

def threat_message(amount):
    messages_data = None
    with open("./keyboard-messages.json") as f:
        messages_data = json.load(f)
    
    for i in range(amount):
        message_chosen = random.choice(messages_data)
        open_app("notepad")
        time.sleep(1)

        for x in range(random.randrange(15, 20)):
            pyautogui.write(message_chosen)
            pyautogui.press("enter")

def destroy_keyboard():
    for x in range(50):
        pyautogui.write(random.choice(string.ascii_lowercase))
        pyautogui.press("enter")
        time.sleep(0.0125)

def end():
    open_app("notepad")
    time.sleep(1)

    for x in range(random.randrange(15, 20)):
        pyautogui.write("YOU JUST GOT TROLLED, I'M SORRY")
        pyautogui.press("enter")

    pyautogui.write("I'm leaving you alone now, peace!")

def alt_f4():
    pyautogui.hotkey("alt", "f4")

def open_app(app_name):
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write(app_name)
    time.sleep(0.5)
    pyautogui.press("enter")
