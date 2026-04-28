import pyautogui
from pynput import keyboard

TEXT_TO_TYPE = "12345"
is_typing = False

def on_press(key):
    global is_typing
    if is_typing:
        return
    try:
        is_typing = True
        pyautogui.write(TEXT_TO_TYPE)
    finally:
        is_typing = False

def on_release(key):
    if key == keyboard.Key.esc:
        print("ESC pressed, exiting...")
        return False

print("AutoTyper started. Press any key to type '12345', press ESC to exit.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()