from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def site_launch():
    return render_template("dz2_vd04.html")
if __name__ == "__main__":
    app.run()