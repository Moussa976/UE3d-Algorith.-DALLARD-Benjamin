from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
        return "Hello my app !"

@app.route('/api/books/',methods=['GET'])
def book():
        book=[{'id':1,'titre' : 'un titre',},{'id':2,'titre': 'un autre titre random',}]
        return jsonify(book)

@app.route('/api/books/<id>',methods=['GET'])
def lebook(id=None):
        leid = int(id)
        book=[{'id':1,'titre' : 'un titre',},{'id':2,'titre': 'un autre titre random',}]

        if(leid == 1):
                data = book[0]
        elif(leid == 2):
                data = book[1]
        else :
                data = book

        return render_template('index.html', title="faite une route qui retourne un book selon son id", data=data)
        #request.json[book[0]['id']][0]
        #return jsonify(book[leid])

if __name__ == "__main__":
        app.run()
