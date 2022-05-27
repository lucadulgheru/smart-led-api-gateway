import requests
import json
from constants import *

ESP32_LED_API = ESP32_BASE_PATH + API_ENDPOINT_LED
ESP32_PING_API = ESP32_BASE_PATH + API_ENDPOINT_PING
ESP32_ENUMERATE_API = ESP32_BASE_PATH + API_ENDPOINT_ENUMERATE
ESP32_EVENTS_API = ESP32_BASE_PATH + API_ENDPOINT_EVENTS

def toggle_led(led_id):
	response = requests.get(ESP32_LED_API + API_ACTION_TOGGLE + "/{}".format(led_id)).text
	return json.loads(response)

def toggle_led_on(led_id):
	response = requests.get(ESP32_LED_API + API_ACTION_ON).text
	return json.loads(response)

def toggle_led_off(led_id):
	response = requests.get(ESP32_LED_API + API_ACTION_OFF).text
	return json.loads(response)

def apply_led_color_change(led_id, color_code):
	response = requests.get(ESP32_LED_API + API_ACTION_COLOR + "/{}".format(led_id) + API_VAR_COLOR_CODE + color_code).text
	return json.loads(response)

def get_available_leds():
	response = requests.get(ESP32_ENUMERATE_API).text
	return json.loads(response)

def ping_esp32():
	response = requests.get(ESP32_PING_API).text
	return json.loads(response)

def get_events():
	response = requests.get(ESP32_EVENTS_API).text
	return json.loads(response)
