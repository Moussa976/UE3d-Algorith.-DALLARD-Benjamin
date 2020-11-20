from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html',nom=os.getenv("NOM", "inconnu"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=600)
