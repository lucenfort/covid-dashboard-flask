import requests
from flask import Flask, render_template

app = Flask(__name__)

# URL da API da COVID-19 do Brasil
url = "https://covid19api.com.br/api/v1/cases?state=SP"

# Dados iniciais
data = {"confirmed": 0, "deaths": 0, "recovered": 0}

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    global data
    data = request.get_json()
    return "Webhook recebido com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
