from flask import Flask, render_template, request

app = Flask(__name__)

# Génère un nombre secret lorsque l'application démarre
nombre_secret = random.randint(1, 10)
essais_restants = 5

@app.route('/')
def index():
    return render_template('index.html', essais=essais_restants)

@app.route('/verifier', methods=['POST'])
def verifier():
    global essais_restants

    essai = int(request.form['essai'])
    essais_restants -= 1

    if essai == nombre_secret:
        message = "Félicitations! Vous avez deviné le nombre secret."
        code = "Le mot de passe est: CLER 1971"
    else:
        if essais_restants == 0:
            message = "Vous avez utilisé tous vos essais. Le jeu est terminé."
            code = ""
        else:
            message = "Désolé, ce n'est pas le bon nombre. Essayez encore."
            code = ""

    return render_template('resultat.html', message=message, code=code, essais=essais_restants)

if __name__ == '__main__':
    app.run(debug=True)
