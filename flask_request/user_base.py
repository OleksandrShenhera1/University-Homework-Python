from flask import Flask, request, jsonify
import requests
user_base = Flask(__name__)

@user_base.route("/user_base", methods=["POST"])
def get_user_base():

    user_pass = {
        "Oleksandr" : 123456,
        "Roma" : 123,
        "Admin" : "admin"
    }
    admin_server_url = "http://127.0.0.1:6000/admin_server"
    try:
        data = request.json
        print("user_base received json...")
        print(data)

        user_name = data.get("user_name")
        user_password = data.get("user_password")
        login_status = ["denied", "success"]
        if user_pass.get(user_name) == user_password:
            data["login_status"] = login_status[1]
            if user_name == "Admin":

                admin_server_response = requests.post(admin_server_url, json=data)
                return jsonify(admin_server_response.json()), 200

            return jsonify(data), 200

        data["login_status"] = login_status[0]
        return jsonify(data), 200

    except Exception as e:
        return jsonify(f"Error {e}."), 500

if __name__=="__main__":
    user_base.run(debug=True, port=8000)