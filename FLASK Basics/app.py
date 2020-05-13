from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "First API running"

app.run(port=400)
