from flask import Flask, request, jsonify
import os

app = Flask(__name__)
latest_data = {}

@app.route("/data", methods=["POST"])
def post_data():
    global latest_data
    latest_data = request.json
    return '', 200

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT env var
    app.run(host="0.0.0.0", port=port)
