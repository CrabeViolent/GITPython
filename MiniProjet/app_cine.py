import database as db
 
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonne:
    def __init__(self):
        self.personne_list = []

# # # Ajouter Personnes
    def ajouter_personne(self, nom, age):
        connexion = db.connexion()
        cursor = connexion.cursor()

        nouveau_user = Personne(nom, age)
        self.personne_list.append(nouveau_user)
        sql = "INSERT INTO Personnes (nom, age) VALUES (%s, %s)"
        cursor.execute(sql, (nouveau_user.nom, nouveau_user.age))

        connexion.commit() ; cursor.close() ; connexion.close()

# # # Afficher LIST 
    def afficher_personnes(self):
        connexion = db.connexion()
        cursor = connexion.cursor()    

        sql = "SELECT * FROM Personnes"
        cursor.execute(sql)
        superliste = cursor.fetchall()
        for personne in superliste:
            print(personne)
            print("|=------------------=|\n")

        cursor.close() ; connexion.close() 

# # # Rechercher personne
    def rechercher_personne(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM Personnes WHERE nom=%s"
        cursor.execute(sql,(nom,))
        personne = cursor.fetchone()
        print(personne)

        cursor.close() ; connexion.close()

# # # Filtrer par age
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
                print("-------------------------------------------\n")
        else:
            print(" AUCUN RÉSULTAT TROUVÉ !")
        cursor.close() ; connexion.close()

class FileAttente:
    def __init__(self):
        self.file_attente = []
        self.file_attente_prioritaire = []

# # # Ajouter personne FileAttente    
    def ajouter_personne_en_attente(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        self.file_attente.append(nom)
        sql = "INSERT INTO FileAttente (nom, grade) VALUES(%s, %s)"
        cursor.execute(sql, (nom, "non-prioritaire"))
        connexion.commit() ; cursor.close() ; connexion.close()

# # # Ajouter personne PRIORITAIRE File Attente
    def ajouter_personne_prioritaire(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        self.file_attente_prioritaire.append(nom)
        sql = "INSERT INTO FileAttente (nom, grade) VALUES(%s, %s)"
        cursor.execute(sql, (nom, "prioritaire"))
        connexion.commit() ; cursor.close() ; connexion.close()

# # # Supprimer personne de attente
    def supprimer_personne_de_attente(self):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM FileAttente WHERE grade='non-prioritaire'"
        cursor.execute(sql)
        self.file_attente = cursor.fetchall()

        sql = "SELECT * FROM FileAttente WHERE grade='prioritaire'"
        cursor.execute(sql)
        self.file_attente_prioritaire = cursor.fetchall()

# # # Si il y a quelqu'un dans la FileAttente prioritaire
        if self.file_attente_prioritaire:
            personne_supprime = self.file_attente_prioritaire.pop(0)
            print(f"La personne {personne_supprime} a bien été supprimée de la file d'attente PRIORITAIRE.")

            sql = "DELETE FROM FileAttente WHERE nom=%s"
            cursor.execute(sql, (personne_supprime,))
            return
        
# # # Sinon, si il y a quelqu'un dans la FileAttente        
        elif self.file_attente:
            personne_supprime = self.file_attente.pop(0)
            print(f"La personne {personne_supprime} a bien été supprimée de la file d'attente. ")

            sql = "DELETE FROM FileAttente WHERE nom=%s"
            cursor.execute(sql, (personne_supprime,))

        else:
            print("\n|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
            print("|   La file d'attente est VIDE !    |")
            print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|\n")
        connexion.commit() ; cursor.close()

class SalleCinema:
    def __init__(self):
        self.capacite = 190
        self.capacite_speciale = 10
        self.places_reserves = []
        self.places_speciales = []

# # # RESERVATIONS
    def reserver_place(self, nom, place):
        connexion = db.connexion()
        cursor = connexion.cursor()

        # # # Verification du nombre de places disponibles     
        sql = "SELECT * FROM reservations WHERE type='ordinaire'"
        cursor.execute(sql)
        liste = cursor.fetchall()
        nb_places = len(liste)


        if nb_places < self.capacite:
            sql = "INSERT INTO reservations (nom,place,type) VALUES(%s,%s,%s)"
            cursor.execute(sql, (nom,place,"ordinaire"))
            print("\n|=-= =-= =-= S U C C È S =-= =-= =-= =-= =-= =-= =-= =-= =-=|")
            print(f"| La place {place} a bien été réservée pour {nom}          |")
            print("|=-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-=|\n")
        else:
            print("\n=-=-=-=-=-=-= É C H E C =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|  Zut.. Il n'y a plus de places disponibles . . .        |")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        
        connexion.commit() ; cursor.close()
        


    def reserver_place_speciale(self, nom, place):
        connexion = db.connexion()
        cursor = connexion.cursor()

        # # # Verification du nombre de places speciales disponibles        
        sql = "SELECT * FROM reservations WHERE type ='special'"
        cursor.execute(sql)
        liste = cursor.fetchall()
        nb_places_speciales = len(liste)

        if nb_places_speciales < self.capacite_speciale:
            sql = "INSERT INTO reservations (nom,place,type) VALUES(%s,%s,%s)"
            cursor.execute(sql, (nom,place,"ordinaire"))
            print("\n|=-= =-= =-= S U C C È S =-= =-= =-= =-= =-= =-= =-= =-=-=-=-=|")
            print(f" La place spéciale {place} a bien été réservée pour {nom}")
            print("|=-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-=-=-=-=|\n")
        else:
            print("\n=-=-=-=-=-=-= É C H E C =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|  Zut.. Il n'y a plus de places spéciales disponibles . . .  |")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

        connexion.commit() ; cursor.close()

    def afficher_places_reservee(self):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM reservations"
        cursor.execute(sql)
        reservations = cursor.fetchall()
        for reservation in reservations:
            print(f"\n Nom : {reservation[0]} || Place : {reservation[1]} || Type : {reservation[2]}")
            print("=--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---=")
        
        cursor.close()

    def nombre_places_disponibles(self):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM reservations WHERE type='ordinaire'"
        cursor.execute(sql)
        nb_places = cursor.fetchall()

        sql = "SELECT * FROM reservations WHERE type='special'"
        cursor.execute(sql)
        nb_places_speciales = cursor.fetchall()

        print("\n|=-= =-= =-= =-= =- PLACES DISPONIBLES -= =-= =-= =-= =-=|")
        print(f"       Places 'ordinaires' disponibles  :  {self.capacite - nb_places}")
        print(f"       Places 'speciales' disponibles   :  {self.capacite_speciale - nb_places_speciales}\n")
        cursor.close()

    def filtrer_reservations_par_personne(self,nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM reservations WHERE nom=%s"
        cursor.execute(sql, (nom))
        all_reservations = cursor.fetchall()
        if all_reservations:
            print(f"\n|=-=-=    TOUT LES RÉSERVATIONS DE :  {nom}  =-=-=|")
            for reservation in all_reservations:
                print(f"   Nom :   {reservation[0]}  |   Place :   {reservation[1]}  |   Type :   {reservation[2]} ")
                print("|---                                                                                 ---|")
        else:
            print("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
            print("|=|   Le nom indiqué n'est pas dans notre liste de réservations  |=|")
            print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|\n")
        cursor.close()

    def annuler_reservations(self, nom):
        connexion = db.connexion()
        cursor = connexion.cursor()

        sql = "SELECT * FROM reservations WHERE nom=%s"
        cursor.execute(sql, (nom))
        all_reservations = cursor.fetchall()
        if all_reservations:
            print(f"\n|=-=-=    RÉSERVATIONS SUPPRIMÉES :  =-=-=|")
            for reservation in all_reservations:
                print(f"   Nom :   {reservation[0]}  |   Place :   {reservation[1]}  |   Type :   {reservation[2]} ")
                print("|---                                                                                 ---|")
        else:
            print("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
            print("|=|   Le nom indiqué n'est pas dans notre liste de réservations  |=|")
            print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|\n")


        sql = "DELETE FROM reservations WHERE nom=%s"
        cursor.execute(sql, (nom,))

        connexion.commit() ; cursor.close()




sallecine = SalleCinema()
sallecine.reserver_place("salut",17)


    
