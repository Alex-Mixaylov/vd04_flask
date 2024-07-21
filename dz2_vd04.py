from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def site_launch():
    return render_template("dz2_vd04.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

# Запуск сайта
app.run()