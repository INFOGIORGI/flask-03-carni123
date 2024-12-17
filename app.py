from flask import Flask,render_template


app = Flask(__name__)
dati=((1,"1",1),(2,"2",2),(5,"3",3))
@app.route("/")
def home():
    return render_template("home.html", titolo="home")


@app.route("/details")
def details():
    return render_template("details.html", titolo="details",dati=dati)


@app.route("/dettagli_scaffale/<id>")
def select(id):
    prodotti_scaffale=[]
    for i in dati:
        if i[1] == id:
            prodotti_scaffale.append(i)
            print("dentro")
    print(prodotti_scaffale)
    return render_template("dettaglio_scaffale.html",titolo="details_scaffale",elementi=prodotti_scaffale)



app.run(debug=True)
