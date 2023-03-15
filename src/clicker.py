import pyautogui
import keyboard

print("Hello! Welcome to the ROTMG autoclicker!")
print("Please place your cursor over the discord channel you wish to rapidly join.")
print("""When ready, hit 'x' to begin autoclicking. Hit 'c' to stop. This will close the clicker.""")

def clicker():
    while True:
        pyautogui.PAUSE = 0.1
        pyautogui.click()
        if keyboard.is_pressed('c'):
            break

keyboard.add_hotkey('x', clicker)
keyboard.wait('x')