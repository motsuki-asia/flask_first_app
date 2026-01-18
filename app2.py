from flask import Flask, request

app = Flask(__name__)


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    # リクエストメソッドの使用
    print(request.method)

    if request.method == "GET":
        return """
        <form action="/login" method="post">
            Password: <input type="text"><br>
            <input type="submit" value="Login">
        </form>
        """
    return "Logged in"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
