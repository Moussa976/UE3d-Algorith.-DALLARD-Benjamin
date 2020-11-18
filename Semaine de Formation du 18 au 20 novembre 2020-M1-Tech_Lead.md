# Semaine de Formation du 18 au 20 novembre 2020 - M1-Tech Lead 

_______________

# Au programme 🤖

* Mercredi 18 novembre : 
	* Streamlit  
	* TP - réalisation d'une data app 

* Jeudi 19 novembre : 
	* Flask
	* TP - réalisation d'une mini api web 

* Vendredi 20 novembre :   
	* flask & docker 
	* TP - réalisation d'une mini api web et conteneurisation docker


# Suivi 📈

Créer un repo github et faire a minima deux pushs par jour (matin : 11h30 & aprem : 16h30) afin que je vois ou vous en êtes et m'envoyer le lien par message privé 👌

_______________

## Le framework [Streamlit](https://www.streamlit.io) 👨‍🎓

### Ce que vous apprendrez dans ce cours
A la suite de ce cours vous pouvez : 

*   Comprendre une relation client serveur 
*   Construire une application streamlit en python 

### La relation client-serveur 

La relation client–serveur désigne un mode de communication à travers un réseau entre plusieurs programmes...[voir plus sur wikipedia](https://fr.wikipedia.org/wiki/Client-serveur). 

Les clients sont souvent des ordinateurs personnels ou des appareils individuels (téléphone, tablette), mais pas systématiquement. Un serveur peut répondre aux requêtes d'un grand nombre de clients.

#### Les requêtes 
Une requête est un échange d'information entre un client et un serveur. Ci-dessus un exemple d'architecture client–serveur : deux clients font leurs requêtes à un serveur via Internet. 

![Exemple d'architecture client–serveur : deux clients font leurs requêtes à un serveur via Internet](https://upload.wikimedia.org/wikipedia/commons/d/db/Modèle-client-serveur.svg)

Dans notre cas on va plus s'intéresser a un type de serveur particulier, les API.  

### Ce que sont les API  

Une API (Application Programmable Interface) est un ensemble de fonctions permettant à une application d'offrir des services à d'autres logiciels. Une API peut être distribué localement dans un programme informatique ou au contraire peut avoir vocation a être utilisée par un plus grand nombre d'acteurs (elle devient donc un serveur).

Dans ce cours nous nous intéressons surtout au API Web, c'est-à-dire celles qui permettent de fournir une interface accessible en ligne. Cela est le cas lorsque l'on effectue une requête à un serveur afin que l'on reçoive le résultat d'un traitement. 

### REST

L'architecture REST est, depuis $10$ ans, une des architectures les plus utilisées. En effet, elle est rapide a mettre en place, extrêmement puissante et répond à une très large majorité des cas. Par exemple, supposons que l'on souhaite un ensemble de programmes (site Web, application Smartphone) permettant de réserver et de gérer ses vols d'avions. Une architecture REST pourrait centraliser les fonctionnalités comme le montre le diagramme suivant.

![Exemple d'architecture REST](https://i.ytimg.com/vi/UQwjytQzoqE/maxresdefault.jpg)


### Les Routes

Les requêtes HTTP se caractérisent par des **routes** : il s'agit d'un chemin permettant de structurer l'accessibilité des opérations. Reprenons l'exemple de gestion de vols d'avions :
- la route http://monserveur.com/list permet de lister les vols disponibles
- la route http://monserveur.com/fly permet d'ajouter ou modifier un vol
- la route http://monserveur.com/action/disconnect permet de déconnecter l'utilisateur
Cette structuration permet ainsi d'organiser toutes les fonctionnalités disponibles via l'API de manière cohérente et ergonomique. Les routes *list*, *fly* et *action/disconnect* sont donc définies par l'architecte logiciel dans le code de l'API.

### Les verbes HTTP

La philosophie de l'architecture REST est de proposer une route permettant d'effectuer un traitement en rapport avec une action précise. Par exemple, la route *fly* permet d'ajouter ou modifier un vol, mais comment spécifie-t-on précisement si l'on souhaite ajouter, modifier ou supprimer un vol ? C'est ainsi que les verbes HTTP ont été conçus pour faciliter cette interaction :

- **GET** effectue une lecture
- **POST** crée une donnée
- **PUT** met à jour une donnée
- **DELETE** supprime une donnée

#### Les principaux codes HTTP 

Lorsque l'on effectue une requête, un code HTTP est automatiquement fourni. Ce code permet d'identifier le résultat d'une requête ou d'indiquer une éventuelle erreur lors du traitement d'une requête. Les plus connues sont :

* 200 : Succès
* 400 : Erreur de syntaxe
* 404 : Introuvable
* 403 : Interdit
* 500 : Erreur interne
	
Lorsque l'on code une API REST, il est fortement conseillé de fournir des codes HTTP spécifiques pour informer les utilisateurs de l'état d'une requête.

Plus d'informations [ici](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) 👀


### Découvrir Streamlit 

Avant de construire une API on va sortir de nos scripts ou de votre jupyter et voir ce que ca peut donner dans un format applicatif. Pour cela on va s'intéresser à un framework python [streamlit](https://www.streamlit.io) qui permet de deployer rapidement des models de machine learning ainsi que des visualisation rapide. 


Vous trouverez ici le cours sur [gist](https://gist.github.com/bdallard/3a7cad831e041950a7703cebe498af55)


## TP : réalisation d'une data app 

votre mission est de construire une petite application de visualisation interactive de données avec l’outil Streamlit vu au chapitre précédent, qui contiendra les fonctionnalités suivantes :   

* Charger des jeux de données (au moins 2) présents dans votre répertoire local
	* il faudra donc que votre application pointe un chemin et sorte les fichier (dataset) du repertoire pointé. Vous utiliserez pour cela le module `os` de python.
* Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur
* Afficher le nom des colonnes du dataset 
* Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées 
* La shape du dataset, par lignes et par colonnes
* Afficher les statistiques descriptives du dataset
* Afficher plusieurs type de graphique dans une partie visualisation avec notamment : 
	* Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
	* Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)

Et enfin une dernière partie dite « visualisation personnalisable » qui permettra de : 

* Sélectionner le type de graphique à tracer
Sélectionner des colonnes dans le jeux de données afin de générer le graphique
* **(bonus)**À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions 🧐

## La librairie Flask 


### Installation 
Vous pouvez installer Flask avec `pip` en suivant la procédure [suivante](https://flask.palletsprojects.com/en/1.0.x/installation/). 


### Ce que vous apprendrez dans ce cours
A la suite de ce cours vous pouvez : 

*   Comprendre le framework FLASK
*   Comment construire des routes
*   Comment créer des templates HTML qu’un navigateur web va pouvoir lire


### A quoi ressemble une application FLASK

Vous allez très souvent démarrer votre application FLASK avec le code suivant dans un script python (par exemple `first_app.py`):


```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
 return "hello world!"
if __name__ == '__main__':
    app.run(debug=True)
```


Ce code peut faire peur au départ mais il n’a rien de compliqué. Prenons le ligne-par-ligne :



1. `From flask import Flask` : Au départ vous importez FLASK comme un librairie classique
2. `app = Flask(__name__)` : Ici, nous créons une instance de la classe Flask à laquelle nous passons le paramètre __name__ qui sert à déterminer le nom de l’application en fonction de si elle est démarrée en tant qu’application ou alors en tant que module d’une application. Si l’application est démarrée en tant qu’application principale __name__ sera égal à “__main__” . Dans le cas inverse, elle aura le nom du fichier dans lequel vous importez votre application
3. `@app.route("/"):` Est ce qu’on appelle un décorateur, on définit en fait l’URL ou une requête via ce décorateur. Tout ce qui sera en dessous de ce décorateur définira ce qu’il faut faire à l’URL que l’on a définit dans la méthode _.route()_. C’est aussi ce qu’on appelle une vue. En l’occurence, dans notre exemple, à chaque fois que nous irons à l’URL racine, nous avons une fonction _index()_ qui retournera “Hello World!”
4. `if __name__ = "__main__" `: Ce code ainsi que ce qu’il y a en dessous permet de dire à Python que vous ferez tourner cette application dès lors qu’elle n’est pas un module d’une autre application mais bien une application à part entière. Plus d'information [ici](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

Ces 4 points regroupent presque l’entièreté de ce que nous devons connaître en Python. Si ceci n’est pas clair encore, c’est normal. Nous allons expliciter dans les parties d’après.

### Faire tourner une application FLASK

Si vous enregistrez le code d’au dessus dans un fichier _app.py_ vous n’aurez plus qu’à le faire tourner sur votre console en utilisant :


```
python app.py
```


Vous devriez avoir la réponse suivante qui apparaît :


```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 618-045-329
```


Si les URL ou PIN ne sont pas les mêmes ce n’est pas grave. L’important étant que vous alliez sur l’URL mis au dessus. Copiez le sur votre navigateur Web. Vous devriez voir votre application live. 

### Les routes


#### Qu’est ce qu’une route ?

Les routes sont des décorateurs qui vous permettent de définir ce qu’il faut faire en fonction de la requête que vous souhaitez faire.

Vous avez bien lu, les routes vous permette de faire des requêtes HTTP. Plus précisément elles définissent l’URL de la requête HTTP. 	


```
@app.route('/about')
def about():
    return 'The about page'
```


Ici par exemple, à chaque fois que nous irons sur l’URL comportant `/about` la fonction nous retournera “The about page”.


### Les méthodes HTTP avec flask

Vous pouvez préciser les méthodes que vous autoriser à l’utilisation. Par défaut les routes ne répondent uniquement qu’à des requêtes GET, vous pouvez ajouter la méthode POST de la façon suivante :


```
@app.route('/, methods=["GET", "POST"])
def index():
    response = get_a_response()
    return response
```


Vous pouvez déterminer la requête via le module _request_ de Flask. Vous pouvez donc appliquer des actions différentes en fonction de si la requête est un POST ou un GET


```
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```


Ici par exemple, si l’utilisateur demande une requête POST alors on effectuera la fonction _do_the_login()_ sinon, on retournera plus la fonction _show_the_login_form()_

NB1 : Ne vous embettez pas à comprendre ce que sont les fonction _do_the_login()_ ou _show_the_login_form()_. Celles-ci sont juste ici pour servir d’illustration

NB2 : N’oubliez pas d’importer le module request comme nous l’avons fait au début du code.



### Les fichiers statiques


#### Comment organiser son dossier

Les fichiers statiques sont les fichiers CSS ou JS que vous ajoutez pour mettre de l’animation ou du style à votre site web. Lorsque vous créez une application FLASK, vous pouvez ajouter un dossier _static_ dans lequel vous aurez vos fichier CSS et JavaScript. 

Pareil pour les fichier `.html` il faut créer un dossier `templates`. 


### Les templates HTML

Avec Flask, vos fichiers HTML sont considérés comme des templates. En effet, on part souvent du principe que vous aurez plusieurs pages HTML dans votre applications et que, par conséquent, vous aurez du code que vous aurez à réutiliser.


#### Créer son dossier _templates_

Avant de commencer à créer vos templates, vous aurez besoin d’un endroit où les mettre. Pour cela, vous aurez besoin d’un dossier que vous appelerez _templates_ 

### Créer un template

Une fois que vous avez créé votre dossier, vous pouvez créer un template html. Chacun des fichiers est un template que vous pourrez réutiliser à souhait dans chacun des autres fichiers HTML que vous allez créer. Pour cela, il suffira d’utiliser la _Jinja2_ qui est la librairies utilisée par Flask pour pouvoir accéder à des variables en back-end. Plus de détail [ici](https://jinja.palletsprojects.com/en/2.11.x/)

Comme vous pouvez voir qu'il s'agit d'écrire du HTML dans un format particulier. A l’intérieur des <body></body> vous pouvez voir :

```
{% block content %}{% endblock %}
```

Ceci est du code en _Jinja2_. Entre ces deux blocs pourra se trouver de l’HTML d’un autre template.

#### Ecrire du Jinja2 dans le template rapidement

Il y a quelques écritures à connaître pour écrire en Jinja2. Voici donc un exemple :


```
<!doctype html>
<title>Hello from Flask</title>
{% if name == True %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```


Si vous souhaitez utiliser une variable, vous pouvez le faire en l’entourant d'accolades. Dans l’exemple du dessus, nous avons une variables _name_ qu’on accède dans


```
<h1> Hello {{ name }} </h1>
```


Cette variable a été définie dans une vue (fichier où l’on trouve toutes les routes).

On peut aussi mettre des conditions et du code via _{% code %}_

En l'occurrence, nous avons créé une condition avec le code suivant :


```
 {% if name == True %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```


Dans cet exemple si notre variable _name_ existe alors on dira _Hello_ _name_ sinon simplement _Hello, World!_

Vous avez maintenant les grandes lignes. Vous pouvez creuser dans les documentations et suivre des tutoriels (ne pas suivre trop de tuto/ressources, on est souvent perdu à la fin). 



## TP Flask 

**Quickstart** 
Ecrire une application flask suivant le modele ci-dessus avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello DC"
* une route qui renvoie "hello name", ou name est une variable string 
	* on devra donc trouver "hello name" à la route (http:localhost:5000/ma_route/name) avec la possibilité de changer la variable name. 
* refaite la meme chose en ajoutant un template 

**Contexte**

Vous avez répondu à l'appel d'offre d'une mairie qui consiste à digitaliser la bibliothèque de la commune. Il faudra pour cela proposer un "catalogue" en ligne de leur ressources et donner la possibilité au utilisateur du site de faire des recherches de livre. On supposera que la bibliothèque nous met à disposition ces livres via un fichier `.json` ci-dessous. 
Vous devez donc construire une api (application flask) avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello my app"
* instancier une variable `book` dans votre aopplication tel que : 
```
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
```
* faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json 
* faite une route qui retourne un book selon son `id` 
* faite une route qui retourne un book selon son titre 
* chager le fichier [books.json](https://drive.google.com/file/d/1UdRCm5d5UAPnfjGes_rHZl2kDQ9NNAsG/view?usp=sharing) et faite de même avec ce fichier
* **(bonus)** écrire un template pour le résultat de la recherche



## Docker 👨‍🎓

Docker est un logiciel libre permettant de lancer des applications dans des conteneurs logiciels.
Il ne s'agit pas de virtualisation, mais de conteneurisation, une forme plus légère qui s'appuie sur certaines parties de la machine hôte pour son fonctionnement. Cette approche permet d'accroître la flexibilité et la portabilité d’exécution d'une application, laquelle va pouvoir tourner de façon fiable et prévisible sur une grande variété de machines hôtes, que ce soit sur la machine locale, un cloud privé ou public, etc. Plus d'information sur la documentation officielle [ici](https://docs.docker.com/v17.09/). 

Docker a été inventé pour résoudre un probleme classique que nous avons tous rencontré en informatique. 
Un meme parle toujours mieux que milles mots : 
<div style="text-align:center">
<img src="https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd">
</div>

### Ce que vous apprendrez dans ce cours
A la suite de ce cours vous pouvez : 

*   Conteneuriser une application python avec Docker 


## TP Docker & Flask 


**Quickstart Docker** 

* comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
* installer docker sur votre machine (Ubuntu de préférence, si pas de machine ubuntu vous pouvez faire un double boot ou bien installer une VM en profitant de l'accès gratuit d'un éditeur cloud GCP, Azur, AWS...) 
* lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
* regarder si votre container est bien lancer 
* faire un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers
	* expliquer les commandes docker `build`, `run` et `exec`
	* expliquer ce qu'est un port dans un container
* vérifier en vous connectant à votre container qu'il est bien `up` et qu'il s'aggit bien 
* **(bonus)** lancer un petit container applicatif en python avec docker 

**Docker et Python**

* écrire un Dockerfile contenant : 
	* Une image ubuntu ou python 
	* installer python3, pip3 et vim 
	* une installation automatique du fichier `requirements.txt` que vous écrirez à la racine de votre application. Renseignez vous sur ce fichier `requirements.txt`, que fait il, pourquoi est il utile? 
	* un repertoire app (dans lequel se trouvera votre application flask) 
	* une exposition du port de votre choix
	* pour finir le container devra lancer votre application flask sur le port de votre choix précédemment exposé.  
	* **(bonus)** déployer votre application sur le cloud gratuit [heroku](https://www.heroku.com)

	
**Projet Bonus facultastif à rendre pour le 02/12**
Coder un site type vitrine/portfolio en flask et le déployer avec github pages 

## Ressources utiles 

- flask doc : https://flask.palletsprojects.com/en/ 1.1.x/ 
- docker doc : https://docs.docker.com 