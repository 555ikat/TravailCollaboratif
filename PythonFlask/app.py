# -*- coding: utf-8 -*-
"""
Site personnel — Application Flask
"""
import os

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)

app = Flask(__name__)
app.secret_key = "changez-moi-en-production"


# Dossier racine : le Bureau de la machine qui exécute Flask.
# Chaque personne qui lance l'app voit donc SON propre Bureau, pas celui du propriétaire du code.
IMAGE_ROOT = os.path.expanduser("~/Desktop")
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def _safe_join_image(relative_path: str) -> str:
    """Construit un chemin absolu sécurisé sous IMAGE_ROOT."""
    root = os.path.abspath(IMAGE_ROOT)
    target = os.path.abspath(os.path.join(root, relative_path))
    if not target.startswith(root):
        abort(404)
    return target


@app.context_processor
def inject_year():
    from datetime import datetime
    return {"current_year": datetime.now().year}


@app.route("/")
def index():
    """Page d'accueil."""
    return render_template("index.html")


@app.route("/a-propos")
def about():
    """Page À propos."""
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Page Contact."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if name and email and message:
            # À brancher sur un envoi d'email réel (SendGrid, etc.)
            flash("Message reçu ! Je vous répondrai dès que possible.", "success")
            return redirect(url_for("contact"))
        flash("Veuillez remplir tous les champs.", "error")
    return render_template("contact.html")


@app.route("/explorateur-images/")
def image_browser():
    """Explorateur d'images dans un dossier local."""
    # Chemin relatif sous IMAGE_ROOT ("" = racine).
    rel_path = request.args.get("p", "").strip().lstrip("/\\")
    current_dir = _safe_join_image(rel_path)

    if not os.path.isdir(current_dir):
        abort(404)

    entries = os.listdir(current_dir)
    subdirs = sorted(
        e for e in entries if os.path.isdir(os.path.join(current_dir, e))
    )
    images = sorted(
        e
        for e in entries
        if os.path.isfile(os.path.join(current_dir, e))
        and os.path.splitext(e)[1].lower() in ALLOWED_IMAGE_EXTENSIONS
    )

    parent_rel = None
    if rel_path:
        parent_rel = os.path.dirname(rel_path)

    return render_template(
        "image_browser.html",
        rel_path=rel_path,
        subdirs=subdirs,
        images=images,
        parent_rel=parent_rel,
    )


@app.route("/explorateur-images/fichier")
def image_file():
    """Renvoie le fichier image demandé (sous IMAGE_ROOT)."""
    rel_path = request.args.get("p", "").strip()
    if not rel_path:
        abort(404)

    full_path = _safe_join_image(rel_path)
    if not os.path.isfile(full_path):
        abort(404)

    return send_file(full_path)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
