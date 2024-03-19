
from flask import flask

app = flask(__name__)

@app.route("/")
def index():
    return "sveiki"
if __name__ == '__main__':
    app.run(part= 5000)

print("sveiki")