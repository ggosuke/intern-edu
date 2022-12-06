from flask import Blueprint, jsonify

# Blueprint
app = Blueprint('test', __name__)

@app.route('/api/test')
def hello():
  message = {}
  data = {}

  message['message'] = 'Test Flask!'
  data['status'] = 200
  data['data'] = message

  return jsonify(data)