# Site personnel — Flask

Site vitrine personnel réalisé avec **Python** et **Flask**.

## Prérequis

- Python 3.10 ou plus récent
- `pip`

## Installation

1. Créer un environnement virtuel (recommandé) :

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   # ou : .venv\Scripts\activate   # Windows
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Lancer le site

```bash
python app.py
```

Ouvrir dans le navigateur : **http://127.0.0.1:5000**

## Structure du projet

- `app.py` — Application Flask et routes
- `templates/` — Modèles Jinja2 (base, accueil, à propos, contact)
- `static/css/style.css` — Styles
- `static/js/main.js` — Menu mobile
- `requirements.txt` — Dépendances Python

## Personnalisation

- Modifier le nom et la description dans `templates/index.html`
- Adapter les textes dans `templates/about.html` si besoin
- Pour envoyer les messages du formulaire par email, brancher un service (SendGrid, Mailgun, etc.) dans la route `contact()` de `app.py`
- En production, définir `app.secret_key` via une variable d’environnement et désactiver le mode debug
