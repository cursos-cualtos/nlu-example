from flask import Flask
import os, json
from nlu import do_analize


app = Flask(__name__, static_url_path='')
port = int(os.getenv('PORT', 8000))

@app.route('/hello')
def hello():
    greeting = {'message': 'Hello world!'}
    return json.dumps(greeting)

@app.route('/nlu')
def nlu():
    return do_analize()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
