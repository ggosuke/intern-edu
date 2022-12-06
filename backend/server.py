from flask import Flask
from flask_cors import CORS
from api import hello, test

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(hello.app)
app.register_blueprint(test.app)

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=80, debug=True)