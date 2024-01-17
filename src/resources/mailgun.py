import os
from pathlib import Path

from dotenv import load_dotenv
import requests

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
DOMAIN = os.getenv('DOMAIN')
API_KEY = os.getenv('API_KEY')


def send_simple_message(to, subject, body):
	return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", API_KEY),
		data={"from": f"Agrima <mailgun@{DOMAIN}>",
			"to": [to],
			"subject": subject,
			"text": body})
 