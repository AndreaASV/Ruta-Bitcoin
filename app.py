"""Flask API para Ruta Bitcoin"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ruta Bitcoin API en funcionamiento"

if __name__ == "__main__":
    app.run(debug=True)