from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def my_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    app.run()