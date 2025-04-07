from flask import Flask, request
from api import translate  # Import the translate.py handler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    return translate.handler(request)

if __name__ == '__main__':
    app.run(debug=True)
