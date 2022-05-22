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
CHANGE_COLOR_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_VAR_LED_ID + API_ACTION_COLOR
PING_ENDPOINT = API_BASE_URL + API_ENDPOINT_PING
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

# LED on endpoint
@app.route(LED_ON_ENDPOINT, methods=["GET"])
@cross_origin()
def led_on(led_id):
	response = ""
	if led_id == '0':
		response = toggle_led_on(led_id)
	return response

# LED off endpoint
@app.route(LED_OFF_ENDPOINT, methods=["GET"])
@cross_origin()
def led_off(led_id):
	response = ""
	if led_id == '0':
		response = toggle_led_off(led_id)
	return response

# Change LED color endpoint
@app.route(CHANGE_COLOR_ENDPOINT, methods=["GET"])
@cross_origin()
def change_color(led_id, color_code):
	response = apply_led_color_change(led_id, color_code)
	return response

# Ping the ESP32 board endpoint
@app.route(PING_ENDPOINT, methods=["GET"])
@cross_origin()
def ping_board():
	response = ping_esp32()
	return response

app.run()
