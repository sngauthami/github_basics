from flask import Flask

app = Flask(__name__)

@app.route('/') 
def home():
    return "Hello, World!"

app.route("/abc")
def abc():
    return "This is the ABC route."


if __name__ == '__main__':
    app.run(debug=True)