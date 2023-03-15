import pyautogui
import keyboard

def clicker():
    while True:
        pyautogui.PAUSE = 0.1
        pyautogui.click()
        if keyboard.is_pressed('c'):
            break

keyboard.add_hotkey('x', clicker)
keyboard.wait('x')