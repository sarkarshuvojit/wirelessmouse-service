from flask import Flask
from net import get_ip_address
from flask import request
import pyautogui

app = Flask(__name__)
print(f"Server Started at {get_ip_address('wlp6s0')}:0.0.0.0")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/move')
def move_cursor():
    x_percent = float(request.args.get('x_percent'))
    y_percent = float(request.args.get('y_percent'))
    screenWidth, screenHeight = pyautogui.size()
    move_x = (x_percent/100) * screenWidth
    move_y = (y_percent/100) * screenHeight
    pyautogui.move(move_x, move_y, duration=1, tween=pyautogui.easeInOutQuad)
    return {}

