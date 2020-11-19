from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
        return "Hello my app !"

@app.route('/api/books/',methods=['GET'])
def book():
        book=[{'id':1,'titre' : 'un titre',},{'id':2,'titre': 'un autre titre random',}]
        return jsonify(book)

@app.route('/api/books/id/<id>',methods=['GET'])
def lebookbyid(id=None):
        leid = int(id)
        book=[{'id':1,'titre' : 'un titre',},{'id':2,'titre': 'un autre titre random',}]

        if(leid == 1):
                data = book[0]
        elif(leid == 2):
                data = book[1]
        else :
                data = book

        return render_template('index.html', title="Les données de book selon son id", data=data)
        #request.json[book[0]['id']][0]
        #return jsonify(book[leid])

@app.route('/api/books/titre/<titre>',methods=['GET'])
def lebookbytitre(titre=None):
        letitre = str(titre)
        book=[{'titre':1,'titre' : 'un titre',},{'titre':2,'titre': 'un autre titre random',}]

        if(letitre == 'un titre'):
                datatitle = book[0]
        elif(letitre == 'un autre titre random'):
                datatitle = book[1]
        else :
                datatitle = book

        return render_template('index.html', title="Les données de book selon son titre", datatitre=datatitle)
if __name__ == "__main__":
        app.run()
