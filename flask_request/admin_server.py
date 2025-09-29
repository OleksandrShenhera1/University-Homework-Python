from flask import Flask, request, jsonify

admin_server = Flask(__name__)

@admin_server.route("/admin_server", methods=["POST"])
def admin_info():
    data = request.json
    print("logged to admin server.")
    data["status"] = "admin"
    print(data)

    return jsonify(data), 200

if __name__=="__main__":
    admin_server.run(debug=True, port=6000)