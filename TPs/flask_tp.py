from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'hello DC'

@app.route('/user/<name>')
def helloname(name=None):
    return "Hello "+name

@app.route('/usertemplate/<name>')
def hellonametemplate(name=None):
    # affichage
    return render_template('index.html', title='Hello template', name=name)

if __name__ == '__main__':
    app.run(debug=True)