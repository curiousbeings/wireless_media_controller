import flask
import ctypes
import time
app=flask.Flask(__name__)

@app.route("/run/<number>",methods=["GET"])
def run_command(number):
	
	num = float(number)		#number is grabbed from the resource of app.route but it is a string so convert to a float
	square=num*num
	response=flask.Response(str(square),headers={"Access-Control-Allow-Origin":"*"})		#The code won't work without this(related to cross origin resource sharing)
	return response