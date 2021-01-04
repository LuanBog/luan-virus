# General Modules
import time
import random
import threading

# Virus Modules
import screenrotator
import mousekeyboard

amount = 10
delay = 0.25

def rotate_screen(amou, dela):
    for i in range(amou):
        direction = random.choice([0, 90, 180, 270])
        screenrotator.change_display_direction(direction)

        time.sleep(dela)

    screenrotator.change_display_direction(0)

def threat_messages(amou):
    mousekeyboard.threat_message(amou)

def mouse_spam(amou, dela):
    mousekeyboard.spam_click(amou, dela)

def screen_mouse():
    screen = threading.Thread(target=rotate_screen, args=(amount, delay,))
    mouse = threading.Thread(target=mouse_spam, args=(amount, delay,))
    screen.start()
    mouse.start()
    # screen.join()
    # mouse.join()


# Main Sequence
if __name__ == "__main__":
    print("-----VIRUS START IN 2 SECONDS-----")
    time.sleep(2)
    
    # Rotates the screen while mouse clicks
    print("[CONTROL] Rotating Screen, Spam Mouse")
    screen_mouse()

    print("[TIMER] 5 seconds")
    time.sleep(5)

    # Sends 1 threat message
    print("[ENLIGHTEN] Enlightening target")
    threat_messages(2)

    # Rotates the screen while mouse clicks 2x
    print("[CONTROL] Rotating Screen, Spam Mouse")
    screen_mouse()
    screen_mouse()

    print("[TIMER] 5 seconds")
    time.sleep(5)

    # Rotates the screen to the right
    print("[CONTROL] Rotate screen to the right")
    screenrotator.change_display_direction(270)
    
    # Literally destroy the keyboard
    print("[CONTROL] Spam keys")
    mousekeyboard.destroy_keyboard()

    for i in range(10):
        print("[KEYBOARD] Alt F4")
        mousekeyboard.alt_f4()
        time.sleep(2)

    print("[CONTROL] Rotating Screen, Spam Mouse")
    screen_mouse()

    print("[TIMER] 10 seconds")
    time.sleep(10)

    # Rotates the screen to the right
    print("[CONTROL] Rotate screen to the right")
    screenrotator.change_display_direction(270)

    # Keeps the screen right for 1 minute (Just to make the victim think that it's forever stuck)
    time.sleep(30)

    # Rotates the screen back to default
    print("[CONTROL] Rotates screen back to default")
    screenrotator.change_display_direction(0)

    # Literally destroy the keyboard
    print("[CONTROL] Spam keys")
    mousekeyboard.destroy_keyboard()

    time.sleep(5)

    print("[TEEHEE] Show the the user got TROLLED LMFAOOO")
    mousekeyboard.end()

    print("-----\"VIRUS\" IS DONE! THANKS FOR WATCHING-----")

