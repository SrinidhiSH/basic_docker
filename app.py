from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Version 1 is made here'

if __name__ == '__main__':
    app.run(debug=True)
