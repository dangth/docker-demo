from flask import Flask
import os
import socket
app = Flask(__name__)
host = socket.gethostname()

@app.route('/')
def hello():
    return "Hello PTIT student!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
