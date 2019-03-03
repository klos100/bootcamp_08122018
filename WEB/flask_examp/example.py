from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html.j2', name='Nieznajomy')



@app.route("/add_user", methods = ['POST']) # pierwszenstwo ma taqka porna przed <name. czyli argumentem który podaje uzytkownik
def add_user():
    return f"Zaraz dodam...{request.form['username']}"


@app.route("/<name>") #przekazywanie argumentu funkcji
def hello_name(name):
    return render_template('main.html.j2', name=name)


if __name__ == "__main__":
    app.run()

