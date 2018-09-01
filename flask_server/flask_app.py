import flask
import pyautogui
import ctypes
import time
import keyboard
app=flask.Flask(__name__)

@app.route("/run/<command>",methods=["GET"])
def run_command(command):
	if command=="change_tab":
		pyautogui.hotkey('alt', 'tab')
		#keyboard.send('alt+tab')
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
	elif key=="press_b":
		pyautogui.press("b")
	elif key=="press_c":
		pyautogui.press("c")
	elif key=="press_d":
		pyautogui.press("d")
	elif key=="press_e":
		pyautogui.press("e")
	elif key=="press_f":
		pyautogui.press("f")
	elif key=="press_g":
		pyautogui.press("g")
	elif key=="press_h":
		pyautogui.press("h")
	elif key=="press_i":
		pyautogui.press("i")
	elif key=="press_j":
		pyautogui.press("j")
	elif key=="press_k":
		pyautogui.press("k")
	elif key=="press_l":
		pyautogui.press("l")
	elif key=="press_m":
		pyautogui.press("m")
	elif key=="press_n":
		pyautogui.press("n")
	elif key=="press_o":
		pyautogui.press("o")
	elif key=="press_p":
		pyautogui.press("p")
	elif key=="press_q":
		pyautogui.press("q")
	elif key=="press_r":
		pyautogui.press("r")
	elif key=="press_s":
		pyautogui.press("s")
	elif key=="press_t":
		pyautogui.press("t")
	elif key=="press_u":
		pyautogui.press("u")
	elif key=="press_v":
		pyautogui.press("v")
	elif key=="press_w":
		pyautogui.press("w")
	elif key=="press_x":
		pyautogui.press("x")
	elif key=="press_y":
		pyautogui.press("y")
	elif key=="press_z":
		pyautogui.press("z")
	return "hey"