# Small pynput script to prevent runtime disconnect on google colab

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from pynput import keyboard

import time
import random

# Use this to get mouse position

# from pynput.mouse import Listener
# def click(x,y,button,pressed):
#     print("Mouse is Clicked at (",x,",",y,")","with",button)
# with Listener(on_click=click) as listener:
#     listener.join()

mouseCont = MouseController()
KeyboardCont = KeyboardController()
stop = False

def click_folder_icon():
	mouseCont.position = (21, 318)
	time.sleep(1)
	mouseCont.click(Button.left, 1)
	time.sleep(2)
	mouseCont.click(Button.left, 1)

def click_cell():
	mouseCont.position = (447, 211)
	time.sleep(2)
	mouseCont.click(Button.left, 1)

def type_message(msg):
	
	KeyboardCont.type(msg)
	time.sleep(2)

	# Delete typed message
	for i in range(len(msg)):
		KeyboardCont.press(Key.backspace)
		KeyboardCont.release(Key.backspace)

def move_mouse_to_random_position():
	# Move to random position between 100 and 700
	x = random.randint(100, 700)
	y = random.randint(100, 700)
	mouseCont.position = (x, y)
	time.sleep(2)

def on_press(key):
	global stop
	try:
		# Press 'q' to quit
		if key.char == 'q':
			stop = True
	except AttributeError:
		pass


if __name__ == '__main__':
	time.sleep(5)

	listener = keyboard.Listener(on_press=on_press)
	listener.start()

	# Continue to do this until 'q' is pressed
	while not stop:
		click_folder_icon()
		click_cell()
		type_message("test")
		move_mouse_to_random_position()
		time.sleep(60)
		move_mouse_to_random_position()
		time.sleep(60)



