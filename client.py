import requests
from constants import *

ESP32_LED_API = ESP32_BASE_PATH + API_ENDPOINT_LED
ESP32_PING_API = ESP32_BASE_PATH + API_ENDPOINT_PING
ESP32_ENUMERATE_API = ESP32_BASE_PATH + API_ENDPOINT_ENUMERATE

# TODO Add toggle through ID

def toggle_led_on(led_id):
	response = requests.get(ESP32_LED_API + API_ACTION_ON).text
	return response

def toggle_led_off(led_id):
	response = requests.get(ESP32_LED_API + API_ACTION_OFF).text
	return response

def apply_led_color_change(led_id, color_code):
	response = requests.get(ESP32_LED_API + API_ACTION_COLOR).text
	return response

def get_available_leds():
	response = requests.get(ESP32_ENUMERATE_API).text
	return response

def ping_esp32():
	response = requests.get(ESP32_PING_API).text
	return response
