from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from fake_useragent import UserAgent
from threading import Thread

print("""
~ Simple Random User Agent Rest API's
----------------------------------------
Created by Bimzzx
----------------------------------------
Follow My Github : github.com/Bimzzx
----------------------------------------""")
app = Flask(__name__)

@app.route('/')
def main():
	user_agent = UserAgent()
	get_user_agent = user_agent.random
	return jsonify({'status': 'success', 'ua_random': get_user_agent})

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
