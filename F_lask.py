from flask import Flask, render_template, request

app = Flask(__name__, template_folder="HTML")

@app.route("/respawn")
def inicio():
    return render_template("respawn.html")

@app.route("/menu")
def sobre():
    return render_template("menu.html")

@app.route("/skins")
def sobre():
    return render_template("skins.html")

@app.route("/mina")
def sobre():
    return render_template("mina.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5500")
