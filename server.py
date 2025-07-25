from flask import Flask, request, jsonify

app = Flask(__name__)
latest_data = {}

@app.route('/data', methods=['POST'])
def post_data():
    global latest_data
    latest_data = request.json
    return '', 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)
