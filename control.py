
import pyautogui # Library to control mouse and keyboard
# pyautogui.PAUSE = 1 # Pause after each PyAutoGUI call
pyautogui.FAILSAFE = True # Move mouse to top-left to abort script

# print(pyautogui.size()) # Get screen size
# print(pyautogui.position()) # Get current mouse position

# Specific location
# for i in range(2): 
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# Any location
# for i in range(2):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)
#     pyautogui.moveRel(-100, 0, duration=0.25) 
#     pyautogui.moveRel(0, -100, duration=0.25)



"""Where is the mouse right now?"""
# import pyautogui
import time
try:
    while True:
        time.sleep(1)
        print(pyautogui.position())

except KeyboardInterrupt:
    print('\nDone.')