from flask import Blueprint, jsonify

# Blueprint
app = Blueprint('hello', __name__)

@app.route('/api/hello')
def hello():
  message = {}
  data = {}

  message['message'] = 'Hello World from Flask!'
  data['status'] = 200
  data['data'] = message

  return jsonify(data)