#!/opt/homebrew/bin/python3

import flask
from flask import request, jsonify
from constants import *

# Endpoint full paths
API_BASE_URL = API_BASE_PATH + API_VERSION
ENUMERATION_ENDPOINT = API_BASE_URL + API_ENDPOINT_ENUMERATE
LED_ON_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_VAR_LED_ID + API_ACTION_ON
LED_OFF_ENDPOINT = API_BASE_URL + API_ENDPOINT_LED + API_VAR_LED_ID + API_ACTION_OFF

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Base path endpoint
@app.route(API_BASE_URL, methods=['GET'])
def home():
	return "<h1>Default path working.</h1>"

# Enumeration endpoint
@app.route(ENUMERATION_ENDPOINT, methods=['GET'])
def enumerate():
	return "<h1>Enumeration endpoint working.</h1>"

# LED on endpoint
@app.route(LED_ON_ENDPOINT, methods=['GET'])
def led_on(led_id):
	return "<h1>Turning on LED with id = " + led_id + "</h1>"

# LED off endpoint
@app.route(LED_OFF_ENDPOINT, methods=['GET'])
def led_on(led_id):
	return "<h1>Turning off LED with id = " + led_id + "</h1>"

app.run()
