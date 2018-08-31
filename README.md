# wireless_media_controller
A web App to control vlc media functions wirelessly using  devices on same network

Using this web app you can run some basic commands supported by vlc like changing volume, toggle full screen in VLC, skip ahead and behind etc.

To run this App you need:
1. Python 2.7
2. Xampp

Setting up the App:
1. Install python 2.7.15 from https://www.python.org/downloads/release/python-2711/
  - pip install virtualenv, pyautogui using "pip install virtualenv pyautogui"(if you have pip configured) or "python -m pip install          virtualenc pyautogui"(if you don't have pip configured)
  - From cmd, cd to any directory and activate a virtual environment by using "virtualenv {ENV}" where dir will be the name of your           virtual environment
  - From cmd, activate the virtual environment using teh command ENV\Scripts\activate
  - run the command "pip install flask" to install flask package
  - paste mediaapp.py into {ENV}(Note: {ENV} is the name of your virtual env)
  
2. Run the Flask server
  -from the activated environment run the command:"set FLASK_APP=0.0.0.0 && flask run --host=0.0.0.0 --port=5000"
  
  
3. Install Xampp from https://www.apachefriends.org/download.html
  - Run xampp from the installed directory (probably c:/xampp)
  - Paste the directories media and keyboard into c:/xampp/htdocs(if the installed location for xampp is different find the htdocs and         paste there)
  - Click on start for Apache service
  - Open your favourite browser and in the url tab enter "http://localhost:80/media/run.html". A webpage with Heading "VLC CONTROLLER!!!"     should appear
  
  Your app is ready to use!!!
  
