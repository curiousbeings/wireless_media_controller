This is a simple example on how a client and server react using REST calls. Here only GET call is explained.
The web client makes call to FLASK server and displays the response

Request made by the web client: GET "http://127.0.0.1:5000/run/<number>" where number is the number entered in the input field
The response is the square of the number.

Download using git bash:
1. Open GIT bash and cd to a directory where you want to place the files.
2. Run the command "git clone https://github.com/curiousbeings/wireless_media_controller.git -b kt".
3. Open CMD and run the command pip install virtualenv.
4. From cmd cd to the folder where the files were cloned and do cd ..
5. Now run the command "virtualenv wireless-media-controller". After insatllation completes run the command "cd wireless-media-controller".
6. Run the command "set FLASK_APP=flasktest.py" and then "flask run --host=0.0.0.0". The flask server is now running. To check it open any browser and type http://127.0.0.1:5000/run/12 The response should be 144.
7. Finally open up another cmd and cd to the folder where the files were cloned and run the command "python -m http.server". Now the web client is active. To check go to http://127.0.0.1:8000/simple_form.html . The web page should render.

Read the code and try to figure out the working.
