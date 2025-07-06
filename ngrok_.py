import os

import time

import json

from pyngrok import ngrok

NGROK_APIKEY = os.environ.get("NGROK_APIKEY", "2IO7jzJGxcT25ynUTomgpwMGuNE_7ae2VeZjMSxHQMNHZrwnY")

ngrok.set_auth_token(NGROK_APIKEY)

uri=ngrok.connect(5900, "tcp")

open("/railway/noVNC/ngrok.txt", "w").write(uri.public_url)

open("/railway/noVNC/ngrok.json", "w").write(json.dumps(uri.data))

while True:

    time.sleep(60*60*24)
