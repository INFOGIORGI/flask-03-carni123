from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", titolo="home")

@app.route("/details")
def details():
    dati=((1,1,1),(2,2,2),(5,3,3))
    return render_template("details.html", titolo="details",dati=dati)


# @app.route("/dettagli_scaffale")

# def select():


app.run(debug=True)
