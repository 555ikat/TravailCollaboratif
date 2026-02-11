# Comment fonctionne Flask — Guide pour justifier le code à l’oral

Ce document t’aide à expliquer chaque partie de ton site Flask de façon claire et technique.

---

## 1. Qu’est-ce que Flask ?

**Flask** est un **micro-framework web** en Python. Il permet de créer une application web en peu de code :

- Le **navigateur** envoie une **requête HTTP** (URL + méthode GET ou POST).
- **Flask** reçoit cette requête, appelle la **fonction** associée à l’URL (la **route**).
- Cette fonction renvoie une **réponse** (souvent une page HTML).

On dit que Flask suit le modèle **MVC** (ou plutôt **MTV** : Model, Template, View) : la **vue** = la fonction Python, le **template** = le HTML généré.

---

## 2. Création de l’application : `app = Flask(__name__)`

```python
app = Flask(__name__)
```

- **`Flask(...)`** : crée l’objet application qui gère routes, requêtes, réponses.
- **`__name__`** : nom du module Python courant (`"app"` quand on lance `app.py`). Flask s’en sert pour savoir où chercher les dossiers `templates/` et `static/` (relatifs à ce fichier).

**À dire à l’oral :**  
*« On crée une seule instance de l’application Flask. En passant `__name__`, Flask sait où est la racine du projet pour charger les templates et les fichiers statiques. »*

---

## 3. Clé secrète : `app.secret_key`

```python
app.secret_key = "changez-moi-en-production"
```

- Utilisée pour **signer** les données stockées en **session** (cookies côté client).
- Indispensable dès qu’on utilise **`flash()`** (les messages flash passent par la session).
- En production, il faut une clé longue et aléatoire (variable d’environnement).

**À dire à l’oral :**  
*« La clé secrète sert à sécuriser la session. Sans elle, les messages flash ne fonctionnent pas correctement et ce n’est pas sécurisé. »*

---

## 4. Les routes : décorateur `@app.route(...)`

```python
@app.route("/")
def index():
    return render_template("index.html")
```

- **Décorateur** : `@app.route("/")` enregistre la fonction `index` pour l’URL **`/`**.
- Quand un utilisateur demande `http://127.0.0.1:5000/`, Flask appelle `index()` et renvoie ce qu’elle retourne.
- **`render_template("index.html")`** : Flask cherche `templates/index.html`, le rend avec le moteur de templates **Jinja2**, et renvoie le HTML généré.

**À dire à l’oral :**  
*« Chaque route associe une URL à une fonction. Ici, la racine du site affiche la page d’accueil en rendant le template `index.html`. »*

---

## 5. Contexte global : `@app.context_processor`

```python
@app.context_processor
def inject_year():
    from datetime import datetime
    return {"current_year": datetime.now().year}
```

- Une **context processor** est une fonction dont le **dictionnaire retourné** est ajouté au **contexte** de **tous** les templates.
- Dans n’importe quel template, on peut écrire `{{ current_year }}` sans passer la variable à chaque `render_template()`.

**À dire à l’oral :**  
*« Au lieu de passer l’année en cours à chaque page, je l’injecte une fois pour toutes via un context processor. Ça évite la répétition et centralise la logique. »*

---

## 6. Formulaire : GET vs POST et `request`

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        # ...
        if name and email and message:
            flash("Message reçu ! ...", "success")
            return redirect(url_for("contact"))
        flash("Veuillez remplir tous les champs.", "error")
    return render_template("contact.html")
```

- **`methods=["GET", "POST"]`** : cette URL accepte les deux types de requêtes. Par défaut Flask n’accepte que GET.
- **GET** : afficher la page (formulaire vide).
- **POST** : envoi du formulaire ; les données sont dans **`request.form`**.
- **`request.form.get("name", "")`** : récupère le champ `name` du formulaire, ou `""` s’il est absent. Le `.strip()` enlève les espaces inutiles.
- **`flash(message, category)`** : enregistre un message dans la **session** ; il sera affiché à la prochaine page (une seule fois).
- **`redirect(url_for("contact"))`** : redirige le navigateur vers l’URL de la fonction `contact`. On redirige après un POST pour éviter de renvoyer le formulaire si l’utilisateur rafraîchit (pattern **Post-Redirect-Get**).

**À dire à l’oral :**  
*« La même URL gère l’affichage du formulaire en GET et l’envoi en POST. Je récupère les champs avec `request.form`, je valide, puis j’affiche un message flash et je redirige pour éviter de renvoyer le formulaire au prochain rafraîchissement. »*

---

## 7. Les templates Jinja2

### Fichier de base : `base.html`

- **`{% block title %}...{% endblock %}`** : bloc que les pages filles peuvent **surcharger** (ex. « Accueil — Mon site »).
- **`{{ url_for('index') }}`** : génère l’**URL** de la route dont le nom de fonction est `index` (ex. `/`). Si tu changes l’URL dans `app.py`, les liens se mettent à jour automatiquement.
- **`{{ url_for('static', filename='css/style.css') }}`** : génère l’URL vers un fichier **statique** (CSS, JS, images).

### Héritage

Dans `index.html` on a par exemple :

```html
{% extends "base.html" %}
{% block title %}Accueil — Mon site personnel{% endblock %}
{% block content %}
  ...
{% endblock %}
```

- **`extends "base.html"`** : le template hérite de la structure de `base.html`.
- On ne redéfinit que les **blocs** (`title`, `content`). Le reste (header, nav, footer, CSS) vient du parent.

**À dire à l’oral :**  
*« J’utilise l’héritage de templates : une base commune (barre de navigation, footer, structure HTML) et chaque page ne définit que son titre et son contenu. `url_for` génère les liens à partir des noms de routes, ce qui évite les erreurs si on change les URLs. »*

---

## 8. Messages flash dans le template

```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class="flash-messages">
      {% for category, msg in messages %}
        <li class="flash flash-{{ category }}">{{ msg }}</li>
      {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

- **`get_flashed_messages(with_categories=true)`** : récupère les messages enregistrés par **`flash()`** et les **consomme** (ils ne réapparaîtront pas).
- **`with_categories=true`** : on récupère aussi la catégorie (`"success"`, `"error"`) pour adapter le style (`flash-success`, `flash-error`).

**À dire à l’oral :**  
*« Les messages flash sont stockés en session. Dans la base, je les affiche une fois avec `get_flashed_messages`, ce qui les supprime de la session. La catégorie permet de les styliser différemment. »*

---

## 9. Point d’entrée : `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

- **`__name__ == "__main__"`** : vrai **uniquement** quand on exécute ce fichier directement (`python app.py`), pas quand on l’importe depuis un autre module.
- **`app.run(debug=True, port=5000)`** : lance le serveur de développement Flask sur le port 5000. **`debug=True`** active le rechargement automatique et les pages d’erreur détaillées (à désactiver en production).

**À dire à l’oral :**  
*« Le serveur ne se lance que si on exécute ce fichier directement. En production, on utilise en général un serveur WSGI comme Gunicorn plutôt que `app.run()`. »*

---

## 10. Récapitulatif du flux

1. L’utilisateur ouvre une URL (ex. `/contact`) ou envoie un formulaire (POST).
2. Flask compare l’URL et la méthode à ses **routes** et appelle la bonne **vue** (fonction).
3. La vue peut lire **`request`** (formulaire, paramètres), utiliser **`flash()`**, puis soit **`return render_template(...)`** (page HTML), soit **`return redirect(...)`** (nouvelle requête).
4. **Jinja2** génère le HTML à partir du template (blocs, `url_for`, `get_flashed_messages`, etc.).
5. Flask renvoie ce HTML (ou la redirection) au navigateur.

---

## Mots-clés à connaître pour l’oral

| Terme | Signification |
|--------|----------------|
| **Route** | Association URL + méthode HTTP → fonction Python |
| **Vue** | La fonction Python qui traite la requête et renvoie la réponse |
| **Template** | Fichier HTML avec du code Jinja2 (`{% %}`, `{{ }}`) |
| **`url_for()`** | Génère l’URL d’une route ou d’un fichier statique |
| **`request`** | Objet qui contient la requête (form, method, args, etc.) |
| **`flash()`** | Enregistre un message affiché une fois (via la session) |
| **Session** | Données stockées côté serveur (ou signées côté client), liées à l’utilisateur |
| **Redirect** | Réponse qui demande au navigateur d’aller vers une autre URL |

Avec ça, tu peux décrire le rôle de chaque partie de ton code et le justifier clairement à l’oral.
