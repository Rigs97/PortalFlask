from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template("paginas/index.html",titulo_pagina="Página inicial")


@app.route('/esportes')
def esportes():
    return render_template("paginas/esportes.html",titulo_pagina="Esportes")


@app.route('/famosos')
def famosos():
    return render_template("paginas/famosos.html",titulo_pagina="Famosos")


@app.route('/politica')
def politica():
    return render_template("paginas/politica.html",titulo_pagina="Politica")


@app.route('/financas')
def financas():
    return render_template("paginas/financas.html",titulo_pagina="Finanças")


if __name__ =="__main__":
    app.run(debug=True)