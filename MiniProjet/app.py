import database as db

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonne:
    def __init__(self):
        self.personne_list = []

    def ajouter_personne(self, nom, age):
        connexion = db.connexion()
        cursor = connexion.cursor()

        nouveau_user = Personne(nom, age)
        self.personne_list.append(nouveau_user)
        sql = "INSERT INTO Personnes (nom, age) VALUES (%s, %s)"
        cursor.execute(sql, (nouveau_user.nom, nouveau_user.age))

        connexion.commit() ; cursor.close() ; connexion.close()

    def afficher_personnes(self):
        connexion = db.connexion()
        cursor = connexion.cursor()    

        sql = "SELECT * FROM Personnes"
        cursor.execute(sql)
        superliste = cursor.fetchall()
        for personne in superliste:
            print(personne)
            print("|=------------------=|")

        cursor.close() ; connexion.close() 

    def rechercher_personne(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM Personnes WHERE nom=%s"
        cursor.execute(sql,(nom,))
        personne = cursor.fetchone()
        print(personne)

        cursor.close() ; connexion.close()

    def filtrer_personne_par_age(self, min_age, max_age):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM Personnes WHERE age BETWEEN %s and %s"
        cursor.execute(sql, (min_age, max_age))
        superliste = cursor.fetchall()
        
        if superliste:
            print(f"Liste des personnes dont l'age est compris entre {min_age} et {max_age}")
            print("=-=  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  =-=")
            for personne in superliste:
                print(f"Nom : {personne[0]} |  Age : {personne[1]}")
                print("-------------------------------------------")
        else:
            print(" AUCUN RÉSULTAT TROUVÉ !")
        cursor.close() ; connexion.close()

class FileAttente:
    def __init__(self):
        self.file_attente = []
        self.file_attente_prioritaire = []
    
    def ajouter_personne_en_attente(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        self.file_attente.append(nom)
        sql = "INSERT INTO FileAttente (nom, grade) VALUES(%s, %s)"
        cursor.execute(sql, (nom, "non-prioritaire"))
        connexion.commit() ; cursor.close() ; connexion.close()

    def ajouter_personne_prioritaire(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        self.file_attente_prioritaire.append(nom)
        sql = "INSERT INTO FileAttente (nom, grade) VALUES(%s, %s)"
        cursor.execute(sql, (nom, "prioritaire"))
        connexion.commit() ; cursor.close() ; connexion.close()

    def supprimer_personne_de_attente(self):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM FileAttente WHERE grade='non-prioritaire'"
        cursor.execute(sql)
        self.file_attente = cursor.fetchall()

        sql = "SELECT * FROM FileAttente WHERE grade='prioritaire'"
        cursor.execute(sql)
        self.file_attente_prioritaire = cursor.fetchall()

        if self.file_attente_prioritaire:
            personne_supprime = self.file_attente_prioritaire.pop(0)
            print(f"La personne {personne_supprime} a bien été supprimée de la file d'attente PRIORITAIRE.")

            sql = "DELETE FROM FileAttente WHERE nom=%s"
            cursor.execute(sql, (personne_supprime,))
        
        elif self.file_attente:
            personne_supprime = self.file_attente.pop(0)
            print(f"La personne {personne_supprime} a bien été supprimée de la file d'attente. ")

            sql = "DELETE FROM FileAttente WHERE nom=%s"
            cursor.execute(sql, (personne_supprime,))

        else:
            print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
            print("|   La file d'attente est VIDE !    |")
            print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
        connexion.commit() ; cursor.close() ; connexion.close()






        




    
