from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World!!!!!<h1>"


@app.route("/goodbye")
def goodbye():
    return "<h1>Good Bye.....!!!!!<h1>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello! {name}</h1>"


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000, debug=True)
