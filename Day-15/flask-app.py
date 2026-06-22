from flask import Flask

app = Flask(__name__) # Creating a flask application instance

@app.route("/")
def hello():
    return 'Hello, world!'

app.run('0.0.0.0')