from flask import Flask, request, jsonify
from datetime import datetime
import requests
client_run = Flask(__name__)

@client_run.route("/client", methods=["POST"])
def client_request():

    try:

        data = request.get_json()

        user_name = data.get("user_name")
        user_password = data.get("user_password")
        browser = data.get("browser")
        framework = data.get("framework")
        request_time = datetime.now()


        user_base_url = "http://127.0.0.1:8000/user_base"
        client_response = {
            "user_name" : user_name,
            "user_password" : user_password,
            "browser" : browser,
            "framework" : framework,
            "request_time" : request_time.strftime("%d/%m/%y"),
        }

        server_response = requests.post(user_base_url, json=client_response)
        return jsonify(server_response.json()), 200

    except Exception as e:
        return jsonify(f"Error f{e}."), 500


if __name__=="__main__":
    client_run.run(debug=True, port=5000)
