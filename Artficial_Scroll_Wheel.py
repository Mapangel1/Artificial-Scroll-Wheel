import pyautogui as pa
from pynput import keyboard
print("Running")
def numpad(key):
    try:
        if key.char == ('+'):
            pa.scroll(300)
        elif key.char == ('-'):
            pa.scroll(-300)
    except AttributeError:
        pass

with keyboard.Listener(on_press=numpad) as listener:
    listener.join()
input("Press enter to exit program...")
