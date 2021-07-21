"""Main application file"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """Test http connection"""
    return "Outro Deploy"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)