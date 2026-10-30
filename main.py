#IMporta o Flask
from flask import Flask,render_template

#Define o objeto principal para a variável 'app'
app = Flask(__name__)

#Define a rota principal
@app.route("/")

#Retorna a dashboard em app.route("/")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)

