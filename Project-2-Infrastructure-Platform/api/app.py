from flask import Flask , jsonify , request
from database import get_connection
from server_service import get_all_servers , get_one_server , create_server

app = Flask(__name__)

@app.route("/servers", methods=["GET"])
def get_servers():
    servers = get_all_servers()
    return jsonify(servers)


@app.route("/servers/<int:server_id>", methods=["GET"])
def get_server_by_id(server_id):
   server = get_one_server(server_id)
   required_fields = ["hostname", "ip_address", "os", "environment"]



   return jsonify(server)


@app.route("/servers", methods=["POST"])
def create_server_endpoint():
    data = request.get_json()
    for field in required_fields:
      if field not in data:
         return jsonify({"error": f"Missing required field: {field}"}), 400
    if server is None:
        return jsonify({"error": "Server not found"}), 404

    server = create_server(
        data["hostname"],
        data["ip_address"],
        data["os"],
        data["environment"]
    )

    return jsonify(server), 201


if __name__ == '__main__':  
   app.run() 