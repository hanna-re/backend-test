from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])  # Replace '*' with your Netlify domain for production

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask on PythonAnywhere!"})

if __name__ == "__main__":
    app.run()
