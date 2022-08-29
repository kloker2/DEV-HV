import requests

token = "5786595330:AAF_BRz5Lx22QJVxHeMATI4R34V1q0LgWxE"
root_url = "https://api.telegram.org/bot"

ok_codes = 200, 201, 202, 203, 204


def send_message(token, chat_id, message):
	url = f"{root_url}{token}/sendMessage"
	res = requests.post(url, data={'chat_id': chat_id, "text": message})
	if res.status_code in ok_codes:
		return True
	else:
		print(f"Request failed with status_code {res.status_code}")
		return False


def get_updates(token):
	url = f"{root_url}{token}/getUpdates"
	res = requests.get(url)
	if res.status_code in ok_codes:
		updates = res.json()
		#result = {"error": None, "data": updates}
		return updates


updates = get_updates(token)
'''
if len(updates["result"]) > 0:
	last_message = updates["result"][-1]
	last_message_text = last_message["message"]["text"]
	chat_id = last_message["message"]["chat"]["id"]
	print(last_message_text)
else:
	print("No messages")
'''
"""
message_id = updates["result"][-1]["message"]["message_id"]
current_message_id = 0
if current_message_id < message_id:
	print("ok")
"""
last_message_id = 0
while True:
	updates = get_updates(token)
	last_message = updates["result"][-1]	
	message_id = last_message["message"]["message_id"]
	
	last_message_text = last_message["message"]["text"]
	chat_id = last_message["message"]["chat"]["id"]	
	
	if message_id > last_message_id:
		send_message(token, chat_id, last_message_text)
		last_message_id = message_id



#send_message(token, chat_id, "Hello bot")

"""
message":{"message_id":3,	"from":{"id":1659557948,
									"is_bot":false,
									"first_name":"Bogdan",
									"last_name":"M",
									"username":"bogda4elo",
									"language_code":"uk"},
									"chat":{"id":1659557948,
											"first_name":"Bogdan",
											"last_name":"M",
											"username":"bogda4elo",
											"type":"private"},
											"date":1658767940,
											"text":"hello"}}]}
"""