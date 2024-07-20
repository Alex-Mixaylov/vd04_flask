from flask import Flask, render_template

app = Flask(__name__)
# @app.route("/")
# @app.route("/<password>/")
#
# def name(password = None):
#     if password == '1234':
#         return f"Доступ разрешен под паролем, {password}"
#     else:
#         return f"Доступ зпрещен"

@app.route("/")
def render():
    return render_template("index.html")
if __name__ == "__main__":
    app.run()