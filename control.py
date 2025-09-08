
# import pyautogui # Library to control mouse and keyboard
# pyautogui.PAUSE = 1 # Pause after each PyAutoGUI call
# pyautogui.FAILSAFE = True # Move mouse to top-left to abort script

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



# import pyautogui
# import time
# try:
#     while True:
#         time.sleep(1)
#         print(pyautogui.position())

# except KeyboardInterrupt:
#     print('\nDone.')



"""Where is the mouse right now?"""
# import pyautogui
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)

# except KeyboardInterrupt:
#     print('\nDone.')



# import pyautogui
# pyautogui.click(100, 100) # Move the mouse to XY coordinates and click.
# pyautogui.click(100, 150, button='left')
# pyautogui.click() # Click the mouse at its current location.
# pyautogui.mouseDown() # Press the mouse button down.
# pyautogui.mouseUp() # Release the mouse button.




# """Draw a spiral in a drawing program""" #http://sumopaint.com/
# import pyautogui
# import time
# from pynput import keyboard

# stop_drawing = False  # flag to stop the loop

# # This function will be called on key press
# def on_press(key):
#     global stop_drawing
#     try:
#         if key == keyboard.Key.esc:  # stop on Esc
#             stop_drawing = True
#             return False  # stop listener
#     except AttributeError:
#         pass

# # Start the keyboard listener in a non-blocking way
# listener = keyboard.Listener(on_press=on_press)
# listener.start()

# time.sleep(5)  # time to switch to drawing program
# pyautogui.click()  # focus on drawing program

# distance = 200
# while distance > 0 and not stop_drawing:
#     pyautogui.dragRel(distance, 0, duration=0.2, button='left')  # right
#     distance -= 5
#     if stop_drawing:
#         break
#     pyautogui.dragRel(0, distance, duration=0.2, button='left')  # down
#     pyautogui.dragRel(-distance, 0, duration=0.2, button='left')  # left
#     distance -= 5
#     if stop_drawing:
#         break
#     pyautogui.dragRel(0, -distance, duration=0.2, button='left')  # up

# print("Drawing stopped!")
# listener.stop()




# import pyautogui
# pyautogui.scroll(5) # Scroll up 5 "clicks"
# pyautogui.scroll(-5) # Scroll down 5 "clicks"
# pyautogui.hscroll(5) # Scroll right 5 "clicks"
# pyautogui.hscroll(-5) # Scroll left 5 "clicks"
# 447/423