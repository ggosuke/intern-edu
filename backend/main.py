from flask import Flask, render_template,jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/api')
def api():
  message = {}
  data = {}

  message['message'] = 'Hello World from Flask!'
  data['status'] = 200
  data['data'] = message

  return jsonify(data)

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=80, debug=True)