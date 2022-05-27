#!/opt/homebrew/bin/python3

import flask
import requests
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from constants import *
from client import *

# Endpoint full paths
API_BASE_URL = API_BASE_PATH + API_VERSION
ENUMERATION_ENDPOINT = API_BASE_URL + API_ENDPOINT_ENUMERATE
LED_ON_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_VAR_LED_ID + API_ACTION_ON
LED_OFF_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_VAR_LED_ID + API_ACTION_OFF
LED_TOGGLE_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_ACTION_TOGGLE + API_VAR_LED_ID
CHANGE_COLOR_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_ACTION_COLOR + API_VAR_LED_ID
PING_ENDPOINT = API_BASE_URL + API_ENDPOINT_PING
EVENTS_ENDPOINT = API_BASE_URL + API_ENDPOINT_EVENTS
RECEIVE_DATA_ENDPOINT = API_BASE_URL + ESP32_RECEIVE_DATA

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

# Base path endpoint
@app.route(API_BASE_URL, methods=["GET"])
@cross_origin()
def home():
	return "<h1>Default path working.</h1>"

# Receive data from board endpoint
@app.route(RECEIVE_DATA_ENDPOINT, methods=["GET"])
@cross_origin()
def receive_data():
	return "TODO"

# Enumeration endpoint
@app.route(ENUMERATION_ENDPOINT, methods=["GET"])
@cross_origin()
def enumerate():
	response = get_available_leds()
	return response

# Toggle LED endpoint
@app.route(LED_TOGGLE_ENDPOINT, methods=["GET"])
@cross_origin()
def led_toggle(led_id):
	response = toggle_led(led_id)
	return response

# Change LED color endpoint
@app.route(CHANGE_COLOR_ENDPOINT, methods=["GET"])
@cross_origin()
def change_color(led_id):
	color_code = request.args.to_dict()["color_code"]
	print(color_code)
	response = apply_led_color_change(led_id, color_code)
	return response

# Ping the ESP32 board endpoint
@app.route(PING_ENDPOINT, methods=["GET"])
@cross_origin()
def ping_board():
	response = ping_esp32()
	return response

# Get the events logged by the ESP32
@app.route(EVENTS_ENDPOINT, methods=["GET"])
@cross_origin()
def events():
	response = get_events()
	return response

app.run()
