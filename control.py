
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



# """Where is the mouse right now? + RGB"""
# import pyautogui
# try:
#     while True:
#         x, y = pyautogui.position()
#         try:
#             pixelColor = pyautogui.screenshot().getpixel((x, y))
#             positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#             positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
#             positionStr += ', ' + str(pixelColor[1]).rjust(3)
#             positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
#         except OSError:
#             positionStr = f'X: {x} Y: {y} RGB: (---, ---, ---)'

#         print(positionStr, end='\r', flush=True)

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



# import pyautogui
# im = pyautogui.screenshot()
# print(im.getpixel((0,0))) # Get the color of a pixel
# print(im.getpixel((100,100)))

# im = pyautogui.screenshot()
# im.getpixel((50, 200))
# pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
# pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))


# import pyautogui
# print(list(pyautogui.locateAllOnScreen('photo.png'))) # Locate an image on the screen


# import pyautogui
# pyautogui.click(320, 455)
# pyautogui.typewrite("print('Hello world!')", interval=0.07) # Type smth automatically

# import pyautogui
# pyautogui.click(180, 145, interval=0.25)
# pyautogui.typewrite('hello.txt', interval=0.07)
# pyautogui.press("enter")
# pyautogui.typewrite('Robots will conquer the world', interval=0.03)



# import pyautogui
# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift') # Press $ symbol
# pyautogui.hotkey('ctrl', 'c') # Hotkey Ctrl+C to copy





# https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform
"""Fill out a form automatically"""
import pyautogui, time

pyautogui.PAUSE = 0.5 # Pause after each PyAutoGUI call
pyautogui.FAILSAFE = True # Move mouse to top-left to abort script
nameField = (497, 451)
submitButton = (474, 634)
submitButtonColor = (240, 240)
submitAnotherLink = (533, 247)

formData = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
     'robocop': 4, 'comments': 'Tell Bob I said hi.'},

    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
     'comments': 'n/a'},

    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
     'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},

    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
     'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]
 
time.sleep(5) # Time to switch to the form window


for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECONDS TO CANCEL <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

print('Entering %s info...' % (person['name']))

# Click the Name field.
pyautogui.click(nameField[0], nameField[1])

# Fill out the Name field.
pyautogui.typewrite(person['name'] + '\t')

# Fill out the Greatest Fear(s) field.
pyautogui.typewrite(person['fear'] + '\t')

# Fill out the Source of Wizard Powers field.
if person['source'] == 'wand':
    pyautogui.typewrite(['down', '\t'])
elif person['source'] == 'amulet':
    pyautogui.typewrite(['down', 'down', '\t'])
elif person['source'] == 'crystal ball':
    pyautogui.typewrite(['down', 'down', 'down', '\t'])
elif person['source'] == 'money':
    pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

# Fill out the RoboCop field.
if person['robocop'] == 1:
    pyautogui.typewrite([' ', '\t'])
elif person['robocop'] == 2:
    pyautogui.typewrite(['right', '\t'])
elif person['robocop'] == 3:
    pyautogui.typewrite(['right', 'right', '\t'])
elif person['robocop'] == 4:
    pyautogui.typewrite(['right', 'right', 'right', '\t'])
elif person['robocop'] == 5:
    pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])