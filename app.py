from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Vasavi! Your Python app is running on port 50000 🎉"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=40000)

