def build_response_object(message, event_type):
	response = {
		"message": message,
		"eventType": event_type,
	}
	return response
