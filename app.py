from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)


fil_klær = open("klær.json", encoding="utf-8")
klær = json.load(fil_klær)

fil_vinyler = open("vinyler.json", encoding="utf-8")
vinyler = json.load(fil_vinyler)

fil_doomsday = open("doomsday.json", encoding="utf-8")
doomsday = json.load(fil_doomsday)

fil_produkter = open("produkter.json", encoding="utf-8")
produkter = json.load(fil_produkter)

fil_kjøpside = open("kjøpside.json", encoding="utf-8")
kjøpside = json.load(fil_kjøpside)

handleliste = {}

@app.route("/")
def index():    
    return render_template("index.html", klær=klær, vinyler=vinyler, doomsday=doomsday)

@app.route("/shop")
def rute_klær():
    return render_template("shop.html", klær=klær)

@app.route("/stream")
def rute_stream():
    return render_template("stream.html")

@app.route("/events")
def rute_events():
    return render_template("events.html")

@app.route("/contact")
def rute_contact():
    return render_template("contact.html")

@app.route("/faq")
def rute_faq():
    return render_template("faq.html")

@app.route("/products/<id>")
def rute_products(id):
    products = produkter[id]
    kjøp = kjøpside[id]
    return render_template("products.html", id=id,products=products, kjøp=kjøp)

@app.route("/cart", methods=["GET", "POST"])
def rute_cart():
    if request.method == "POST":
        id = request.form.get("id")
        handleliste[id] = produkter[id]
        return render_template("/cart.html", data=handleliste)
    else:
        return render_template("/cart.html", data=handleliste)

@app.route("/cart/delete/<id>")
def rute_slett(id):
    handleliste.pop(id)
    return redirect("/cart")

@app.route("/checkout/<id>", methods=["GET", "POST"])
def rute_checkout(id):
    products = produkter[id]
    kjøp = kjøpside[id]
    return render_template("checkout.html",id=id,products=products, kjøp=kjøp)
   
@app.route("/purchased/<id>")
def rute_purchased(id):
    products = produkter[id]
    kjøp = kjøpside[id]
    return render_template("purchased.html",id=id,products=products, kjøp=kjøp)


app.run(debug=True, port=5555)