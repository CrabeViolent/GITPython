from flask import Flask, request, render_template, session, redirect, url_for
from employes.employeDAO import EmployeDao
from employes.employe import Employe
from departements.departementDao import DepartementDao
from departements.departement import Departement


app = Flask(__name__)
app.secret_key = 'crabe'

# Accueil
@app.route("/")
def accueil():
    if "username" in session:
        return render_template("accueil.html", username=session["username"])
    else:
        return render_template("accueil.html")

# À propos
@app.route("/about")
def about():
    if "username" in session:
        return render_template("about.html", username=session["username"])
    else: 
        return render_template("about.html")

# Login pour authentification
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Perform authentication
        if username == "admin" and password == "crabe":
            session["username"] = username  # Store the username in the session
            return redirect(url_for("accueil"))  # Redirect to the home page after login
        else:
            return render_template("login.html", message="error")
    else:
        return render_template("login.html", message="info")
    
# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)  # Remove the username from the session
    return redirect(url_for("accueil"))  # Redirect to the home page after logout

@app.route("/services")
def services():
    if "username" in session:
        return render_template("services.html", username=session["username"])
    else: 
        return render_template("services.html")


@app.route('/employes')
def employes():
    if "username" in session:
        message,superliste = EmployeDao.get_all()
        return render_template("employes.html", superliste=superliste, message=message, username=session["username"])
    else:
        return redirect(url_for("login"))  # Redirect to the login page if not logged in

@app.route('/departements')
def departements():
    if "username" in session:
        message, superliste = DepartementDao.get_all()
        return render_template("departements.html", superliste=superliste, message=message, username=session["username"])
    else:
        return redirect(url_for("login"))  # Redirect to the login page if not logged in


@app.route('/ajout-employe')
def ajout_employe():
    if "username" in session:
        return render_template('ajout-employe.html', username=session["username"])
    else:
        return redirect(url_for("login"))  # Redirect to the login page if not logged in
    


@app.route('/traitement', methods=["POST"])
def traitement():
    data = request.form
    nom = data.get("nom")
    prenom = data.get("prenom")
    matricule = data.get("matricule")
    fonction = data.get("fonction")
    departement = data.get("departement")

    if nom == "" or prenom == "" or matricule == "" or fonction == "" or departement == "":
        return render_template("ajout-employe.html", message="error")
    else:
        superliste = EmployeDao.get_all_matricule()
        if (matricule,) in superliste:
            return render_template("ajout-employe.html", message="duplicate")
        else:
            employe = Employe(nom, prenom, matricule, fonction, departement)
            message = EmployeDao.add(employe) 
            return render_template("ajout-employe.html", message=message)

@app.route('/ajout-departement')
def ajout_departement():
    if "username" in session:
        return render_template('ajout-departement.html', username=session["username"])
    else:
        return redirect(url_for("login"))  # Redirect to the login page if not logged in


@app.route('/traitement-departement', methods=["POST"])
def traitement_departement():
    data = request.form
    nom = data.get("nom")
    emplacement = data.get("emplacement")
    direction = data.get("direction")

    if nom == "" or emplacement == "" or direction == "":
        return render_template("ajout-departement.html", message="error")
    else:
        superliste = DepartementDao.get_all_nom()
        if (nom,) in superliste:
            return render_template("ajout-departement.html", message="duplicate")
        else:
            departement = Departement(nom, emplacement, direction)
            message = DepartementDao.add(departement) 
            return render_template("ajout-departement.html", message=message)
        

        
    
