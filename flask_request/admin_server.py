from flask import Flask, request, jsonify
import psycopg2

admin_server = Flask(__name__)

def db_connector():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="mysql"
    )

def create_table(table_name):
    connect = db_connector()
    cursor = connect.cursor()

    cursor.execute(f"""
                   CREATE TABLE IF NOT EXISTS {table_name}
                   (
                       id SERIAL PRIMARY KEY,
                       admin_name TEXT NOT NULL,
                       admin_msg TEXT NOT NULL,
                       created_at TIMESTAMP DEFAULT NOW()
                    );
    """)

    connect.commit()
    cursor.close()
    connect.close()

def add_db_message(user, msg, table_name):
    connect = db_connector()
    cursor = connect.cursor()

    cursor.execute(
            f"INSERT INTO {table_name} (admin_name, admin_msg) VALUES (%s, %s);",
            (user, msg)
    )
    connect.commit()

    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connect.close()


@admin_server.route("/admin_server", methods=["POST"])
def admin_info():
    connect = db_connector()
    cursor = connect.cursor()

    data = request.json
    print("logged to admin server.")
    msg = data.pop("user_message")
    data["admin_message"] = msg
    data["status"] = "admin"
    print(data)

    create_table("admin_messages")

    add_db_message("Admin", msg, "admin_messages")

    return jsonify(data), 200

if __name__=="__main__":
    admin_server.run(debug=True, port=6000)