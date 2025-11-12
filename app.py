from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from Cloud Run — Flask app is working!"

if __name__ == '__main__':
    # Cloud Run sets the PORT environment variable automatically
    port = int(os.environ.get("PORT", 8080))
    # ✅ Must listen on 0.0.0.0 — NOT localhost
    app.run(host="0.0.0.0", port=port)
