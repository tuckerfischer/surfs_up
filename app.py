from flask import Flask

app = Flask(__name__)
@app.route('/')
def hollo_world():
    return 'Hello world'