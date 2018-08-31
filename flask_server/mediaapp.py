import flask
import pyautogui
import ctypes
import time
import keyboard
app=flask.Flask(__name__)

@app.route("/run/<command>",methods=["GET"])
def run_command(command):
	if command=="change_tab":
		#pyautogui.hotkey('alt', 'tab')
		keyboard.send('alt+tab')
	elif command=="vol_up":
		pyautogui.press("volumeup")
	elif command=="vol_down":
		pyautogui.press("volumedown")
	elif command=="fullscreen":
		pyautogui.press("f")
	elif command=="vol_mute":
		pyautogui.press("volumemute")
	elif command=="add_3sec":
		pyautogui.hotkey("shift","right")
	elif command=="add_10sec":
		pyautogui.hotkey("altleft","right")
	elif command=="add_1min":
		pyautogui.hotkey("ctrl","right")
	elif command=="add_5min":
		pyautogui.hotkey("altright","right")
	elif command=="sub_3sec":
		pyautogui.hotkey("shift","left")
	elif command=="sub_10sec":
		pyautogui.hotkey("altleft","left")
	elif command=="sub_1min":
		pyautogui.hotkey("ctrl","left")
	elif command=="sub_5min":
		pyautogui.hotkey("altright","left")
	elif command=="play_pause":
		pyautogui.press("space")
	return "hey"

@app.route("/keyboard/<key>",methods=["GET"])
def keyboard(key):
	if key=="press_a":
		pyautogui.press("a")
	return "hey"
	return "hey"