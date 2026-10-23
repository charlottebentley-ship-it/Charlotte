# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "Bienvenue sur le site de Charlotte 🚀!"


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return """
    <h1>Bienvenue sur le site de Charlotte 🚀!</h1>
    <p>Je me présente, je m'appelle Charlotte Bentley, je suis étudiante en <strong>deuxième année en école d'ingénieur</strong>.</p>
    <h2>Ce que j'aime</h2>
    <ul>
        <li>L'équitation</li>
        <li>La musique</li>
        <li>Et le sport bien sûr</li>
    </ul>
    <img src="https://thumb.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_ICAM_-_2008.svg/1280px-Logo_ICAM_-_2008.svg.png?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=thumbnail" width="100">
    """
# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
